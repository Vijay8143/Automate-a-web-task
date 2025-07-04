# Instagram Automation Bot 🤖

This project automates the process of:
- Logging into Instagram using a dummy account
- Navigating to a target profile (`@cbitosc`)
- Following the account (if not already followed)
- Extracting profile information:
  - Bio
  - Number of Posts
  - Followers
  - Following
- Saving the data to a text file (`cbitosc_profile.txt`)

---

## 🚀 Features

- Automatic login via Selenium WebDriver
- Intelligent follow detection and button interaction
- Robust XPath extraction for dynamic Instagram UI
- Saves profile data in a readable format

---

## 📦 Requirements

- Python 3.8+
- Google Chrome (latest)
- ChromeDriver (auto-managed)

---

## 🛠️ Setup Instructions

1. **Clone this repository** or download the script files.

2. **Install dependencies** using pip:

   ```bash
   pip install selenium webdriver-manager


3.Replace Instagram credentials in dummy.py:

USERNAME = 'your_dummy_username'
PASSWORD = 'your_dummy_password'

4.Run the script:

python dummy.py



---

## 📸 Preview

Below is a sample of the profile bio and data fetched from the `@cbitosc` Instagram profile:

<img src="Preview/Screenshot 2025-06-26 203039.png" alt="Instagram Bio Preview" width="400"/>

This data was extracted and saved automatically to `cbitosc_profile.txt` using Selenium.
