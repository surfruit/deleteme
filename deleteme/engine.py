import sys
import asyncio
import aiohttp
import csv
import time
from fpdf import FPDF
from colorama import Fore, init, Style
from .sites import SITES_DATA

init(autoreset=True)

# Updated GDPR Art. 17 Template with Deleteme branding
GDPR_REQUEST_BODY = """
Subject: Right to Erasure Request (Art. 17 GDPR) via Deleteme
To the Privacy/Legal Team,

I am writing to formally request the permanent deletion of my account and all associated personal data from your service.
Target Username: {username}

Under Article 17 of the General Data Protection Regulation (GDPR), I am exercising my right to be forgotten. 
Please purge all logs, profile information, and tracking data.
This request was generated using the Deleteme Open-Source Privacy Tool.
"""

async def check_site(session, name, data, username, results):
    url_template, delete_link = data
    url = url_template.format(username)
    try:
        async with session.get(url, timeout=7, allow_redirects=True) as response:
            if response.status == 200:
                print(f"{Fore.GREEN}[+] FOUND: {name}")
                results.append({
                    "service": name, 
                    "profile_url": url, 
                    "deletion_url": delete_link,
                    "legal_notice": GDPR_REQUEST_BODY.format(username=username).strip()
                })
    except Exception:
        pass

def generate_exports(username, results):
    # 1. CSV (Optimized for Google Sheets management)
    csv_filename = f"deleteme_audit_{username}.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["service", "profile_url", "deletion_url", "legal_notice"])
        writer.writeheader()
        writer.writerows(results)

    # 2. PDF Report with Deleteme branding
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 20, "Deleteme: Privacy Audit Report", ln=True, align="C")
    
    pdf.set_font("Helvetica", size=10)
    pdf.cell(0, 10, f"Username: {username} | Date: {time.ctime()}", ln=True, align="C")
    pdf.ln(10)
    
    for entry in results:
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, f" Platform: {entry['service']} ", ln=True, fill=True)
        
        pdf.set_font("Helvetica", size=9)
        pdf.write(6, f"Profile: {entry['profile_url']}\n")
        pdf.write(6, f"Manual Removal: {entry['deletion_url']}\n")
        
        pdf.ln(2)
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 4, entry['legal_notice'])
        pdf.set_text_color(0, 0, 0)
        pdf.ln(8)
    
    pdf_filename = f"deleteme_report_{username}.pdf"
    pdf.output(pdf_filename)
    return csv_filename, pdf_filename

async def start_engine():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python -m deleteme.engine <username>")
        return

    target = sys.argv[1]
    found_profiles = []
    
    print(f"\n{Fore.WHITE}{Style.BRIGHT}Deleteme v1.1.0 - Open-Source Privacy Shield")
    print(f"{Fore.CYAN}[*] Searching for digital traces of: {Fore.WHITE}{target}")
    print("-" * 60)

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, name, data, target, found_profiles) 
                 for name, data in SITES_DATA.items()]
        await asyncio.gather(*tasks)
        
    duration = time.time() - start
    
    if found_profiles:
        csv_p, pdf_p = generate_exports(target, found_profiles)
        print("-" * 60)
        print(f"📊 Scan finished in {Fore.YELLOW}{duration:.2f}s")
        print(f"📂 Reports saved: {Fore.WHITE}{pdf_p}, {csv_p}")
        print(f"{Fore.GREEN}[!] Review your reports to start the deletion process.")
    else:
        print(f"{Fore.RED}[-] No traces found for this identity.")

def run():
    asyncio.run(start_engine())

if __name__ == "__main__":
    run()