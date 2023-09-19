from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
uni_name="Stanford University"
keywords=["Courses","Data Mining","Data Base","Teacher Assistent","Work Experience"]

options.add_argument("user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data\\")

#options.add_argument("--profile-directory=Default")
prefs = {"profile.managed_default_content_settings.images": 2}
options.page_load_strategy = 'normal'
# chrome_options = webdriver.ChromeOptions()

# page = webdriver.Chrome(executable_path=chromedriver_path, options=options)
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(service=service)

if __name__ == '__main__':
    
    driver.get("https://app.gomoonbeam.com/headstart/clfy2u6v6104908kwgmqu086t/details")
    sleep(5)
    #essay=driver.find_element(by=By.CSS_SELECTOR,value="#modal-root > div:nth-child(1) > div > div > div.w-full.lg\:w-\[80\%\].h-full.relative.z-10 > div > div > div.mx-auto.mt-10 > div > button:nth-child(1) > div")
    # essay=driver.find_element(by=By.XPATH,value='//*[@id="modal-root"]/div[1]/div/div/div[2]/div/div/div[2]/div/button[1]/div')
    # print(essay)
    # essay.click()
    # sleep(10)

    ## First Page 

    title=driver.find_element(by=By.CSS_SELECTOR,value="#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div.h-auto.min-h-16.mb-16 > div > h1")
    title.send_keys("Statement of purpose")
    sleep(10)
    University=driver.find_element(by=By.CSS_SELECTOR,value="#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div:nth-child(4) > div > p")
    University.send_keys(uni_name)
    sleep(10)
    key_enter=driver.find_element(by=By.XPATH,value='//*[@id="modal-root"]/div[1]/div/div/div[1]/div[4]/div/ul/li/p')
    key_enter.send_keys("First")
    sleep(1)
    key_enter.send_keys(Keys.ENTER)
    sleep(1)
    for key in keywords:
        key_enter.send_keys(key)
        
        key_enter.send_keys(Keys.ENTER)
        sleep(1)
    sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
   
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-root"]/div[1]/div/div/div[2]/button')))
    GenerateButton=driver.find_element(by=By.XPATH,value='//*[@id="modal-root"]/div[1]/div/div/div[2]/button')
    sleep(3)
    GenerateButton.click()
    sleep(10)


    ## Second page


    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    createButton=driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/div/div[2]/button')
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div[2]/button')))
    sleep(3)
    createButton.click()
    sleep(5)

    ## Third Page

    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(10)
    EndButton=createButton=driver.find_element(by=By.XPATH,value='//*[@id="modal-root"]/div[1]/div/div/div[2]/div/button')
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-root"]/div[1]/div/div/div[2]/div/button')))
    sleep(3)
    EndButton.click()
    sleep(5)

    ## Last page 
    Sop_text=driver.find_element(by=By.XPATH,value='//*[@id="modal-root"]/div[2]/div/div/div/div[3]/div')
    sleep(3)

    ## Convert to text And Write Sop  
    with open("Sop.txt", "w") as file:
        file.write(Sop_text.text)
        file.close()
    print(Sop_text.text)
    page_source = driver.page_source
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(page_source)
        file.close()