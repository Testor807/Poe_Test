# Install selenium with pip install selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Poe_Controller():
    def __init__(self):
        # Set Chromeself.options() 
        self.options = webdriver.ChromeOptions()
        # Adding argument to disable the AutomationControlled flag 
        self.options.add_argument("--disable-blink-features=AutomationControlled") 
        #self.options.add_argument("--headless")
        # Exclude the collection of enable-automation switches 
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

        self.options.add_argument('lang=zh_CN.UTF-8')
        self.options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.63 MQQBrowser/8.9 Mobile Safari/537.36')
        self.options.add_experimental_option("detach", True)
                            
        # Turn-off userAutomationExtension 
        self.options.add_experimental_option("useAutomationExtension", False) 
        self.driver = webdriver.Chrome(options=self.options) 
        
        # Send the request 
        self.driver.get("https://www.Poe.com")

    def Login(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/button[1]'))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        ).send_keys("deatherngai@gmail.com")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]'))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys("67078826Ngai")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]'))
        ).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="submit_approve_access"]'))
        ).click()
        #time.sleep(2)
        #WebDriverWait(self.driver, 10).until(
        #    EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button'))
        #).click()

    def Anaylsis_Content(self,img):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[1]/div/div[3]/div/div[1]/textarea'))
        ).send_keys('Extract text from the uploaded image')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[1]/div/div[3]/div/input'))
        ).send_keys(img)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[1]/div/div[3]/div/button[2]'))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/div/div[1]/textarea'))
        ).send_keys('Fill in the review text and write the review feedback')
        time.sleep(3)
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/div/button[2]'))
        ).click()
        time.sleep(10)
        class_l = self.driver.find_elements(By.CLASS_NAME, 'Markdown_markdownContainer__Tz3HQ')
        n = len(class_l)
        print(n)
        rect_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div/div/div['+str(n-1)+']/div[2]/div[2]/div[2]/div/div[1]/div/div')
        feedback_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div/div/div['+str(n)+']/div[2]/div[2]/div[2]/div/div[1]/div/div')
        self.writeTxt('Result.txt',rect_text.get_attribute("textContent"),"Extract Result: \n")
        self.writeTxt('FeedBack.txt',feedback_text.get_attribute("textContent"),"FeedBack: \n")
    
    def writeTxt(self,file,content,title):
        with open(file, 'w') as f:
            f.write(title)
            f.write(content)
        
        #print("Detected Text: "+rect_text.text)
        #print("FeedBack Text: "+feedbacl_text.text)
        #return rect_text.text, feedbacl_text.text
    
    def getResult(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/aside[1]/div/div/menu/section[1]/li[1]'))).click()
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div/div/div[4]/section[1]/button[1]')))
        print(button.is_enabled())
        class_l = self.driver.find_elements(By.CLASS_NAME, 'Markdown_markdownContainer__Tz3HQ')
        n = len(class_l)
        print(n)
        rect_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div/div/div['+str(n-1)+']/div[2]/div[2]/div[2]/div/div[1]/div/div')
        feedback_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div/div/div['+str(n)+']/div[2]/div[2]/div[2]/div/div[1]/div/div')
        #print("React: "+rect_text.get_attribute("textContent"))
        #print("Feed: "+feedback_text.get_attribute("textContent"))
        self.writeTxt('Result.txt',rect_text.get_attribute("textContent"),"Extract Result: \n")
        self.writeTxt('FeedBack.txt',rect_text.get_attribute("textContent"),"FeedBack: \n")
    
    def writeTxt(self,file,content,title):
        with open(file, 'w') as f:
            f.write(title)
            f.write(content)

Poe = Poe_Controller()
#Poe.Login()
#Poe.Anaylsis_Content()
#Poe.getResult()


