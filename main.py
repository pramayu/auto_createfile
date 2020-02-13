import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

path = r"D:\dava_auto_port\utils\chromedriver.exe"
options = ChromeOptions()
options.add_experimental_option("debuggerAddress","127.0.0.1:63111")
driver = webdriver.Chrome(path, options=options)
hasil = open(r"D:\get_lurusin\utils\hasil.txt","a+")


# main code

class LetsGoo:

    def __init__(self, _odp, _service, _port):
        self._odp = _odp
        self._port = _port
        self._service = _service

    def letsinput(self):
        driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/omzetAccessNetwork')
        driver.find_element_by_id("servid").clear()
        if self._service[0] == '3':
            driver.find_element_by_id("servid").send_keys(f"0{self._service}")
        else:
            driver.find_element_by_id("servid").send_keys(self._service)
        driver.find_element_by_id("servid").send_keys(Keys.ENTER)
        time.sleep(3)
        # lengths_service = len(driver.find_elements_by_name("selecteds"))
        # for length_service in range(lengths_service):
        service_name = driver.find_element_by_id("tdserviceinfo1")
        splitstring  = service_name.text
        time.sleep(1)
        driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint')
        time.sleep(2)
        driver.find_elements_by_id("filter")[5].click()
        driver.find_elements_by_id("deviceLocation")[0].send_keys(self._odp)
        driver.find_elements_by_id("deviceLocation")[0].send_keys(Keys.ENTER)
        time.sleep(1)
        elements = driver.find_elements_by_css_selector("td.column_number a")[0]
        driver.find_element_by_link_text(f"{elements.text}").click()
        time.sleep(1)
        odp_name = driver.find_elements_by_class_name("label")[3]
        final_odp = odp_name.text
        if self._service[0] == '3':
            finalservice = f"{splitstring.split()[0]}_RFS;0{self._service};{final_odp};{final_odp}-{self._port}"
        else:
            finalservice = f"{splitstring.split()[0]}_RFS;{self._service};{final_odp};{final_odp}-{self._port}"
        hasil.write(f"{finalservice}\n")
        print(finalservice)
        