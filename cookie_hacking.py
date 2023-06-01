from time import sleep
from a_selenium2df import get_df # pip install a-selenium2df
import undetected_chromedriver as uc # pip install undetected-chromedriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import json
# Para baixar cookies: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
with open(r"C:\Users\hansc\Downloads\mail.tm_cookies (3).json", 'r',encoding='utf-8') as file:
    cookies = json.load(file)
for cookie in cookies:
    if 'sameSite' not in cookie:
        cookie['sameSite'] = 'None'
    if cookie['sameSite'] == 'unspecified':
        cookie['sameSite'] = 'Strict'
    if cookie['sameSite'] == 'lax' or cookie['sameSite'] == 'no_restriction':
        cookie['sameSite'] = 'Lax'
if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get(r"https://mail.tm")
    input()
    while True:
        try:
            df = get_df(driver, By, WebDriverWait, expected_conditions, queryselector="*", with_methods=True, )
            try:
                df.loc[df.aa_id == 'logout'].iloc[0].se_click()
            except Exception:
                pass
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            sleep(5)
        except KeyboardInterrupt:
            break
