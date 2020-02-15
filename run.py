import time
import json
from tqdm import tqdm
from main import LetsGoo
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

with open('utils\sterserah.json','r') as data_file:
    data = json.load(data_file)

# automation code here ...
path = 'utils\chromedriver.exe'
options = ChromeOptions()
# options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = webdriver.Chrome(path)

email = input("Enter dava email: ")
password = input("Enter dava password: ")

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
        loop = tqdm(total = len(data))
        for datax in data:
            letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'], driver)
            letsgo.letsinput()
            loop.set_description(f"Latest Service {datax['SERVICE']}".format(datax))
            loop.update(1)
            
        loop.close()
    else:
        print("Email or Password incorrect!")

else:
    print("Email or Password incorrect!")
