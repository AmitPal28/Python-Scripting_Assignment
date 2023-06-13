from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait







options =  webdriver.ChromeOptions()
#options.add_argument("--headless") 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


chromedriver_path = "C:/Users/amitk/Desktop/Amit_Pal/Python-Scripting_Assignment/chromedriver_win32.exe"

user_district = input("Enter district:")
os.environ["PATH"] += os.pathsep + chromedriver_path


driver = webdriver.Chrome(options= options)
driver.get("https://ceoelection.maharashtra.gov.in/searchlist/")



district_select = driver.find_element(By.ID, "ctl00_Content_DistrictList")
district_select.send_keys(user_district)


time.sleep(2)  # Adjust the delay as needed

# Select other options
assembly_select = driver.find_element(By.ID, "ctl00_Content_AssemblyList")
assembly_select.click()  # Select the appropriate index for the assembly constituency
time.sleep(1)
'''
assembly_option = driver.find_element(By.XPATH, """//*[@id="ctl00_Content_AssemblyList"]/option[1]""")
assembly_option.click()  # Click on the desired assembly constituency option
'''

assembly_select = driver.find_element(By.ID, "ctl00_Content_AssemblyList")
assembly_select.send_keys(Keys.ARROW_DOWN)  # Select the appropriate index for the assembly constituency

type_of_revision_input = driver.find_element(By.ID, "ctl00_Content_listrollrevision_0")
type_of_revision_input.send_keys(Keys.ARROW_DOWN)   # Assuming index 1 corresponds to SSR 2023


# Select SSR 2023 and Marathi language
driver.find_element(By.ID, "ctl00_Content_listrollrevision_0").click() 


driver.find_element(By.ID, "ctl00_Content_LangTypepdf_0").click()

parts_select = driver.find_element(By.ID, "ctl00_Content_PartList")


select_element = Select(parts_select)
total_parts = len(select_element.options)


for i in range(1, total_parts):
    parts_select.click()
    time.sleep(1)# Wait for the website to update
    part_option = driver.find_element(By.XPATH, """//*[@id="ctl00_Content_PartList"], 'Part {i}')]""")
    part_option.click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']"))) 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="aspnetForm"]/div[3]/article/table/tbody/tr[6]/td[2]/img"""))).click()

    # Bypass captcha (Note: This may not always work and might require additional methods)
    captcha_input = driver.find_element(By.ID, "ctl00_Content_txtcaptcha")
    captcha_input.send_keys("bypass_captcha_value")  # Replace with the appropriate value to bypass captcha
    
    # Download PDF
    driver.find_element(By.ID, "ctl00_Content_OpenButton").click()
    time.sleep(2)  # Allow time for the download to complete

    driver.quit()

