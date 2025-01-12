from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    #browser.get('https://www.csdn.net/')
    browser.get("https://www.ticketmaster.co.uk/")
    # 获取远程链接的地址
    #print('remote_url:', browser.caps['goog:chromeOptions']['debuggerAddress'])
    #print('session_id:', browser.session_id)
    #print(browser.title)
    time.sleep(10)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
    ).click()

