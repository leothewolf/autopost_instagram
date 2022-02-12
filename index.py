from itertools import count
from selenium import webdriver
import time
import warnings

import dd_selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from os import listdir
from os import getcwd
from os.path import isfile, join

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

username = "xxx"
password = "xxx"
comment = "xxx"

post_count = 1 #don't alter


def login(user,passw):
    time.sleep(2)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    username = driver.find_element_by_name("username")
    username.click()
    username.send_keys(user)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    password = driver.find_element_by_name("password")
    password.click()
    password.send_keys(passw)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    login_btn= driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
    login_btn.click()

    time.sleep(5)

def post(post_path,comment):
    global post_count
    global total_files

    print("Posting [" + str(post_count) + "/" + str(total_files) + "] post...")

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    post_btn= driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div')
    post_btn.click()

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    post_select = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')

    dd_selenium.dds(post_select, post_path)

    time.sleep(5)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings
    n_1 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
    n_1.click()

    time.sleep(2)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings
    n_1 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
    n_1.click()

    time.sleep(2)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings

    cmt = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
    cmt.click()

    cmt.send_keys(comment)

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings
    n_1 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
    n_1.click()


    def mini_fun():
        try:
            warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings
            a = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/h2")
        except:
            time.sleep(2)
            mini_fun()
    
    mini_fun()

    print("Posted successfully")

    warnings.filterwarnings("ignore", category=DeprecationWarning) #added to suppress warnings
    close1 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/button/div")
    close1.click()
    
    print("Exited post window.")


login(username,password)

#Getting list of files in uploads
cur = getcwd() 
path = cur + "\\uploads"

files = listdir(path)

total_files = 0

for i in files:
    total_files += 1

for i in files:
    v = path + "\\" + i
    post(v,comment)

    time.sleep(30) #30 secs gap between posts -- you can reduce this but it is recommended to keep it 30 or more to avoid detection

driver.quit()
