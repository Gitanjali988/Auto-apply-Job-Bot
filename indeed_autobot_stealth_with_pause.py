import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Your details
FULL_NAME = "Fnu Gitanjali"
EMAIL = "g.geetofficial@gmail.com"
PHONE = "2016585993"
RESUME_PATH = r"C:\Users\User\Downloads\Project\Resume\resume.pdf"
JOB_KEYWORDS = ["Data Analyst", "Data Engineer", "Business Analyst", "Power BI Developer"]

# Start Chrome with stealth settings
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
driver = uc.Chrome(options=options)

print("🚀 Opening Indeed...")
driver.get("https://www.indeed.com")

input("🛑 Please complete the CAPTCHA in browser if prompted. Press ENTER when ready to continue...")

for role in JOB_KEYWORDS:
    print(f"🔍 Searching for: {role}")
    driver.get(f"https://www.indeed.com/jobs?q={role.replace(' ', '+')}&l=")
    time.sleep(4)

    jobs = driver.find_elements(By.CSS_SELECTOR, 'a.tapItem')
    print(f"🧾 Found {len(jobs)} jobs")

    for job in jobs[:3]:  # Limit for demo
        job.click()
        time.sleep(2)
        try:
            driver.switch_to.window(driver.window_handles[-1])
            if "apply" in driver.page_source.lower():
                print("✅ Ready to apply (simulated)")
                # You could fill forms here
            else:
                print("❌ No direct apply button found.")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print("⚠️ Error while applying:", e)

print("✅ Finished.")
driver.quit()
