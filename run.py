import time
from tqdm import tqdm
from main import LetsGoo
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

path = 'utils\chromedriver.exe'
options = ChromeOptions()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = webdriver.Chrome(path)

data = [
    {
        "ODP": "ODP-BLI-FF/04",
        "SERVICE": "17240580077",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/69",
        "SERVICE": "172405803097",
        "PORT": "2"
    },
]


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
            loop.set_description("Loading...".format(datax))
            loop.update(1)
        loop.close()
    else:
        print("Email or Password incorrect!")

else:
    print("Email or Password incorrect!")
