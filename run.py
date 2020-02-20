import os
import time
import json
from tqdm import tqdm
from main import LetsGoo
from f_0430 import CheckBulk
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

print('''
///////////////////////////////////////////////////////////////////////////////////
///                                                                             ///
///     Attention!!                                                             ///
///     Before you use this software, Chrome Web Browser                        ///
///     has installed on your PC.                                               ///
///                                                                             ///
///     How Use this Software ?                                                 ///
///     1. Prepare the xlsx file and rename file as terserah.xlsx               ///
///     2. Visit https://www.aconvert.com/document/xls-to-json/                 ///
///        to convert xlsx to json, download json file and put on utils         ///
///        directory, rename as terserah.json                                   ///
///     3. Type python run.py                                                   ///
///     4. Waiting until the process finish                                     ///
///                                                                             ///
///////////////////////////////////////////////////////////////////////////////////
''')

# open file...



email = input("Enter dava email: ")
password = input("Enter dava password: ")
option = input('''Ngapain ?? 
    1.Lurusin data
    2.Ngecek status bulk
    Pilih 1 atau 2: ''')

if option == "1":
    with open('utils\sterserah.json','r') as data_file:
        data = json.load(data_file)
elif option == "2":
    pathhasil = os.getcwd()
    dateinput = input("Input tanggal bulk, exp: 18-Feb-2020: ")
    with open('utils\oblkstatus.json','r') as data_file:
        data = json.load(data_file)
    hasil = open(pathhasil+r'\utils\hasil.txt',"a+")



# automation code here ...
path = 'utils\chromedriver.exe'
options = ChromeOptions()
# options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = webdriver.Chrome(path)

driver.maximize_window()
driver.get('https://emas.telkom.co.id/DAVA/auth/viewlogin')
time.sleep(2)
current_url = driver.current_url


if len(email) != 0 and len(password) != 0:

    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("btn-primary").click()

    if current_url != driver.current_url:
        time.sleep(2)
        if option == "1":
            loop = tqdm(total = len(data))
            for datax in data:
                letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'], driver)
                letsgo.letsinput()
                loop.set_description(f"Latest Service {datax['SERVICE']}".format(datax))
                loop.update(1)
        elif option == "2":
            driver.get('https://emas.telkom.co.id/DAVA/monitoring/bulkOperation/BulkOperationRequest/')
            driver.find_elements_by_class_name("select2-selection")[0].click()
            time.sleep(2)
            driver.find_elements_by_css_selector("li.select2-results__option")[1].click()
            time.sleep(5)
            driver.find_elements_by_class_name("select2-selection")[1].click()
            time.sleep(2)
            driver.find_elements_by_css_selector("li.select2-results__option")[1].click()
            driver.find_elements_by_id("filter")[1].click()
            driver.find_element_by_name("datetime").send_keys(dateinput)
            driver.find_elements_by_class_name("btn-warning")[0].click()
            time.sleep(3)
            loop = tqdm(total = len(data))
            for dataq in data:
                f_0431 = CheckBulk(driver, hasil, dataq['_id'])
                f_0431.checkstatus()
                loop.set_description(f"Latest Service {dataq['_id']}".format(dataq))
                loop.update(1)
        loop.close()
    else:
        print("Email or Password incorrect!")

else:
    print("Email or Password incorrect!")
