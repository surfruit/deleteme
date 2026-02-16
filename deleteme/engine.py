import sys
import asyncio
import time
import csv
import json
from fpdf import FPDF

# Імпорт бази сайтів
try:
    from .sites import SITES_DATA
except (ImportError, ValueError):
    from deleteme.sites import SITES_DATA

# Шаблон листа GDPR
GDPR_TEMPLATE = """
Subject: Right to Erasure (Art. 17 GDPR) - Request for Data Deletion
To whom it may concern,
I am writing to request the permanent deletion of my account and all associated personal data. 
Nickname: {username}
According to Art. 17 GDPR, I have the right to be forgotten. Please confirm once complete.
"""

async def check_site(session, name, url_template, delete_url, username, found_list):
    url = url_template.format(username)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        async with session.get(url, timeout=10, headers=headers) as response:
            if response.status == 200:
                print(f"✅ [FOUND] {name:15}")
                found_list.append({
                    "site": name, 
                    "profile": url, 
                    "delete_link": delete_url,
                    "gdpr": GDPR_TEMPLATE.format(username=username).strip()
                })
    except:
        pass

async def main_scan():
    if len(sys.argv) < 2:
        print("\n👻 DELETEME\nВикористання: deleteme <username>")
        return

    username = sys.argv[1]
    print(f"\n🔎 Глибокий OSINT-скан для: {username}")
    print("-" * 50)
    
    start_time = time.time()
    found_list = []

    try:
        import aiohttp
    except ImportError:
        print("❌ Помилка: Встанови бібліотеку: python -m pip install aiohttp")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, n, u, d, username, found_list) for n, (u, d) in SITES_DATA.items()]
        await asyncio.gather(*tasks)

    end_time = time.time()
    print("-" * 50)
    print(f"📊 Результат: знайдено {len(found_list)} профілів за {end_time - start_time:.2f} сек.")

    if not found_list:
        print("🤷 Слідів не знайдено.")
        return

    # --- 1. Збереження CSV (для Google Sheets) ---
    csv_file = f"table_{username}.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=["site", "profile", "delete_link", "gdpr"])
        writer.writeheader()
        writer.writerows(found_list)

    # --- 2. Збереження TXT (швидкий звіт) ---
    txt_file = f"report_{username}.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(f"DELETEME REPORT: {username}\n" + "="*30 + "\n\n")
        for item in found_list:
            f.write(f"Сайт: {item['site']}\nПрофіль: {item['profile']}\nВидалити: {item['delete_link']}\n\n")

    # --- 3. Збереження PDF (офіційний документ) ---
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", 'B', 16)
        pdf.cell(0, 10, f"Privacy Audit: {username}", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Helvetica", size=10)
        for item in found_list:
            pdf.set_font("Helvetica", 'B', 11)
            pdf.cell(0, 8, f"Service: {item['site']}", ln=True)
            pdf.set_font("Helvetica", size=9)
            pdf.multi_cell(0, 6, f"URL: {item['profile']}\nDelete: {item['delete_link']}\n")
            pdf.ln(4)
        
        pdf_file = f"report_{username}.pdf"
        pdf.output(pdf_file)
        print(f"📄 Створено PDF: {pdf_file}")
    except Exception as e:
        print(f"⚠️ Не вдалося створити PDF: {e}")

    print(f"📊 Створено CSV: {csv_file}")
    print(f"📝 Створено TXT: {txt_file}")

def scan():
    try:
        asyncio.run(main_scan())
    except Exception as e:
        print(f"❌ Критична помилка: {e}")

if __name__ == "__main__":
    scan()