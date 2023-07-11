from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from turtle import back
from unicodedata import name
import credential as c
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities as u
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



#sample input
author_name = 'Ford, Kevin'

# setup
option = webdriver.ChromeOptions()
toolsURL = "https://mathscinet-ams-org.proxy2.library.illinois.edu/mathscinet/2006/mathscinet/index.html"
option.add_argument("headless")
#base_path = os.path.dirname(os.path.abspath(__file__))
#drive_path = os.path.abspath(base_path + "/chromedriver")
#driver = webdriver.Chrome(drive_path)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(toolsURL)
time.sleep(0.2)


# login
driver.find_element_by_xpath("//*[@id='i0116']").click()
time.sleep(0.2)
driver.find_element_by_id("i0116").send_keys(c.username)
time.sleep(0.2)

driver.find_element_by_xpath("//*[@id='idSIButton9']").click()

time.sleep(0.5)

driver.find_element_by_id("i0118").send_keys(c.password)

time.sleep(5) # wait 0.2 seconds, waiting for the program to get everything 


driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
time.sleep(10)
#try:

def get_author_name(name):
    url = 'https://mathscinet-ams-org.proxy2.library.illinois.edu/mathscinet/search/authors.html?authorName={}&Submit=Search'.format(name)
    time.sleep(10)

    driver.execute_script("window.open('');")


    driver.switch_to.window(driver.window_handles[1])


    driver.get(url)
        
    time.sleep(10)
    try:
        result_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.authorName.important"))
        )
        print(result_name.text)
        result_text = result_name.text
    except:
        print(name)
        print("Multiple name possible, please re-check your input")
        result_text = None

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    return result_text

get_author_name('Ford, Kevin B.')