import sys
import requests
from .sites import SITES_DATA

def scan():
    if len(sys.argv) < 2:
        print("\n👻 DELETEME v0.1.0")
        print("Usage: deleteme <username>")
        return

    username = sys.argv[1]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    print(f"\n🔎 Scanning digital footprint for: {username}")
    print("-" * 60)

    found_sites = []

    for name, (url_template, delete_url) in SITES_DATA.items():
        url = url_template.format(username)
        try:
            res = requests.get(url, timeout=5, headers=headers)
            if res.status_code == 200:
                print(f"✅ [FOUND] {name:12} | Link: {url}")
                found_sites.append((name, delete_url))
            else:
                print(f"   [ ] {name:12} | Not found")
        except:
            print(f"⚠️  [ERROR] {name:12} | Connection failed")

    print("-" * 60)
    print(f"📊 Summary: Found {len(found_sites)} profiles.")

    if found_sites:
        print("\n🧨 DELETION GUIDE:")
        for name, del_link in found_sites:
            print(f"   - To delete {name:10}: {del_link}")
    
    print("\n💡 Tip: Use 'git add .' and 'git commit' to update your GitHub repo!")

if __name__ == "__main__":
    scan()