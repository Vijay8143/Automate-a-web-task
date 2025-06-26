from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace these with your dummy Instagram credentials
USERNAME = 'your_dummy_username'
PASSWORD = 'your_dummy_password'
TARGET_PROFILE = 'cbitosc'

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

try:
    # 1. Open Instagram login
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    # 2. Log in
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(7)

    # 3. Go to the target profile
    driver.get(f"https://www.instagram.com/{TARGET_PROFILE}/")
    time.sleep(5)

    # 4. Try to click the Follow button (safely)
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//header//section//button')))
        follow_clicked = False

        for btn in buttons:
            btn_text = btn.text.lower()
            if 'follow' in btn_text and not any(word in btn_text for word in ['following', 'requested']):
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", btn)
                print(f"✅ Clicked Follow button: {btn.text}")
                follow_clicked = True
                time.sleep(2)
                break

        if not follow_clicked:
            print("❌ Follow button not found or already followed.")
    except Exception as e:
        print(f"❌ Error while trying to follow: {e}")

    # 5. Extract bio (robust)
    time.sleep(3)
    try:
        bio = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"x1q0g3np") and contains(@class,"x78zum5")]')
        )).text
    except:
        bio = "Bio not found"

    # 6. Extract stats: posts, followers, following
    try:
        stats_xpath = '//ul[contains(@class, "_ac2a")]/li//span//span'
        stats = wait.until(EC.presence_of_all_elements_located((By.XPATH, stats_xpath)))
        posts = stats[0].text
        followers = stats[1].text
        following = stats[2].text
    except:
        posts = followers = following = "Data not found"

    # 7. Save profile data
    profile_data = f"""
Instagram Profile: @{TARGET_PROFILE}
Bio: {bio}
Posts: {posts}
Followers: {followers}
Following: {following}
"""

    with open("cbitosc_profile.txt", "w", encoding='utf-8') as f:
        f.write(profile_data.strip())

    print("✅ Profile data saved to cbitosc_profile.txt")

finally:
    driver.quit()
