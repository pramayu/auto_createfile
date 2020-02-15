<<<<<<< HEAD
import os
import csv
import time
from datetime import datetime
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

<<<<<<< HEAD
path = r"C:\Users\gedep\Downloads\auto_createfile-master\auto_createfile-master\utils\chromedriver.exe"
options = ChromeOptions()
options.add_experimental_option("debuggerAddress","127.0.0.1:62781")
driver = webdriver.Chrome(path,options=options)
# hasil = open(r"D:\get_lurusin\utils\hasil.txt","a+")
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd


# main code

class LetsGoo:

<<<<<<< HEAD
    def __init__(self, _odp, _service, _port, _lengthdata, _count):
        self._odp = _odp
        self._port = _port
        self._count = _count
        self._service = _service
        self._lengthdata = _lengthdata

    def createfile(self, length_services, splitstring1, splitstring2, final_odp):
        today = datetime.now()
        strname = today.strftime("%Y%m%d%H%M%S")
        filename = f'data\RFS_UPDATESTP_{strname}.csv'
        with open(filename, 'w', newline='') as f:
            thewriter = csv.writer(f, delimiter='|')
            thewriter.writerow(['   SERVICE_NAME','SERVICE_NUMBER','ODP_PANEL','PORT_NAME'])
            if len(length_services) == 2:
                thewriter.writerow([f'{splitstring2},{splitstring1}',f'{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
            elif len(length_services) == 1:
                if self._service[0] == '3':
                    thewriter.writerow([f'{splitstring1}',f'0{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
                else:
                    thewriter.writerow([f'{splitstring1}',f'{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
        


    def letsinput(self):
        persen = 0
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
        driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/omzetAccessNetwork')
        driver.find_element_by_id("servid").clear()
        if self._service[0] == '3':
            driver.find_element_by_id("servid").send_keys(f"0{self._service}")
        else:
            driver.find_element_by_id("servid").send_keys(self._service)
        driver.find_element_by_id("servid").send_keys(Keys.ENTER)
<<<<<<< HEAD

        time.sleep(3)

        length_services = driver.find_elements_by_name("selecteds")
        if len(length_services) == 2:
            sf1 = driver.find_element_by_id("tdserviceinfo1").text
            splitstring1 = sf1.split()[0]
            sf2 = driver.find_element_by_id("tdserviceinfo2").text
            splitstring2 = sf2.split()[0]
        elif len(length_services) == 1:
            sf1 = driver.find_element_by_id("tdserviceinfo1").text
            splitstring1 = sf1.split()[0]
            splitstring2 = None
        
        time.sleep(1)
        # go to odp
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
        driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint')
        time.sleep(2)
        driver.find_elements_by_id("filter")[5].click()
        driver.find_elements_by_id("deviceLocation")[0].send_keys(self._odp)
        driver.find_elements_by_id("deviceLocation")[0].send_keys(Keys.ENTER)
        time.sleep(1)
<<<<<<< HEAD
        elements = driver.find_elements_by_css_selector("td.column_number a")[0].text
        driver.find_element_by_link_text(f"{elements}").click()
        time.sleep(1)
        odp_name = driver.find_elements_by_class_name("label")[3]
        if elements == "16":
            txt = odp_name.text
            final_odp = txt.split('|', 1)[1]
        else:
            final_odp = odp_name.text
        self.createfile(length_services, splitstring1, splitstring2, final_odp)
        persen = self._count / self._lengthdata * 100
        print(f'Progress: {persen}%')
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
