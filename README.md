<div align="center">
  <h1>👻 Deleteme</h1>
  
  <p>Take back your privacy. Find and delete old accounts — fast.</p>
  
  <br>
  
  ![Version](https://img.shields.io/badge/version-0.1.0-blue?style=for-the-badge&logo=python)
  ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
  ![Python](https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white)
  
</div>

---

### Mission
Deleteme is an OSINT tool that helps find your old accounts by username on 100+ platforms and provides direct links to deletion pages (where they exist).
Inspired by Sherlock, but with a different focus: not just find, but actually erase the traces.

---

### Quick Start

```# 1. Clone the repository
git clone https://github.com/surfruit/deleteme.git
cd deleteme

# 2. Install (recommended in a virtual environment)
pip install .

# 3. Run
deleteme your_username

# Example:
deleteme potus
```

---
### Features
<p>🕵️‍♂️ Deep username search across 100+ platforms (socials, forums, gaming, paste sites…)</p>
<p>🔗 Direct deletion links where they officially exist</p>
<p>🛡️ Privacy-first — runs 100% locally, nothing sent anywhere</p>
<p>⚡ Fast, lightweight, terminal-native</p>
<p>🌈 Colored, readable output</p>

---

### Roadmap

- [ ] Email-based scanning (in addition to username)
- [ ] Data breach / leak checking (Have I Been Pwned style)
- [x] Basic username search implemented
- [ ] Auto-generated GDPR / CCPA deletion request templates
- [ ] Simple local web UI

---

### Contributing – Adding a new site
1. Open deleteme/sites.py
2. Add entry to SITES dict:
   ```"SERVICE_NAME": {
    "url": "https://example.com/user/{}",
    "delete_url": "https://example.com/account/delete",
    "method": "GET",               # or "POST"
    "notes": "May require deleting posts first"},
   ```
3.(optional) Adjust check_account_exists() if needed
<br>
4. Open PR: feat: added Example.com support

---
### License
MIT
---
### Disclaimer
For lawful use only — deleting your own accounts or ones you have explicit permission to delete.
Not responsible for misuse, ToS violations or legal issues.
Use responsibly. 👻
---


