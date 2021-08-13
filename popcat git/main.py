#import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from os import system
from tqdm import tqdm 
from time import sleep
from timeit import default_timer
browser = int(input("Enter the amount of browser iteration: "))
click = int(input("Click per browser(usually its 1000): "))
def clear():
    system('cls')
useless = 0
ua = UserAgent()
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('-log-level=3')
chrome_options.add_argument("-incognito")
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--disable-dev-shm-usage")
clear()
for i in range (0, browser):
    useless1 = 0
    user_agent = ua.random 
    chrome_options.add_argument(f'user-agent={user_agent}') 
    driver = webdriver.Chrome(
        r"C:/Users/edber/Downloads/Popcat project/chromedriver.exe", options=chrome_options)
    driver.get("https://popcat.click/")
    driver.minimize_window()
    element = driver.find_element(By.ID, "app")
    print("Clicking in browser number",useless + 1,"/", browser)
    useless - 1
    print("User agent:",user_agent)
    sleep(3)
    start = default_timer()
    for useless1 in tqdm(range(click)):
        element.click()
        useless1 = useless1 + 1
    stop = default_timer()
    driver.quit()
    result = round(stop - start,2)
    pps = round(useless1/result,2)
    useless = useless + 1
    print("Time:", result)
    print("PPS", pps)
    print("Browser number",useless,"done")
    print("Clicked: ", useless1)
    print("========================================================================================================================================================")
    print("")
print("End of script")