# 🤖 Auto Apply Job Bot (Stealth Mode)

I created this project to fully automate job application bot designed to apply to job listings on **Indeed** within minutes of posting — without being blocked by bot detection mechanisms.

---

## 📌 What This Project Does

- 🔍 Scrapes live job listings from Indeed based on your selected roles
- 🤖 Bypasses "Additional Verification Required" walls using `undetected-chromedriver`
- 🧠 Auto-fills your name, email, phone number, and uploads your resume
- ⚙️ Clicks "Apply Now" or "Easily Apply" buttons and submits forms
- 📬 Sends you an email log of applied jobs (optional)
- ⏸️ Pauses for CAPTCHA if needed, allowing you to complete it manually

---

## 🎯 Why I Built This

As an active job seeker, I noticed many jobs receive hundreds of applicants within hours. To stay ahead of the competition, I created this tool to apply automatically to:
- Data Analyst
- Data Engineer
- Business Analyst
- Business Intelligence roles

This helps me apply faster and spend more time preparing for interviews.

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the bot
```bash
python indeed_autobot_stealth_with_pause.py
```

> 🛑 On the first job search, you'll be prompted to complete the CAPTCHA manually.

---

## ⚙️ Configuration

Edit the top of the script to set your personal details:
```python
FULL_NAME = "Fnu Gitanjali"
EMAIL = "gxxxxx@gmail.com"
PHONE = "2016xxxxx"
RESUME_PATH = r"C:\Users\User\Downloads\Project\Resume\resume.pdf"
JOB_KEYWORDS = ["Data Analyst", "Data Engineer", "Business Analyst", "Power BI Developer"]
```

---

## 📬 Optional: Email Report

If enabled, the bot will send you a summary of applications to your Gmail inbox.
You must generate an [App Password](https://support.google.com/accounts/answer/185833) for this to work.

---

## 🧠 What I Learned

- Handling Selenium bot detection with `undetected-chromedriver`
- Web scraping with dynamic waits
- Automating real-world tasks like job applications
- Gmail automation via Python's SMTP

---

## ✅ License
© 2025 Fnu Gitanjali – All rights reserved.
