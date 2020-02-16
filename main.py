import os
import csv
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys

# hasil = open(r"D:\get_lurusin\utils\hasil.txt","a+")



# main code

class LetsGoo:
    def __init__(self, _odp, _service, _port, _driver):
        self._odp = _odp
        self._port = _port
        self._driver = _driver
        self._service = _service


    def createfile(self, length_services, splitstring1, splitstring2, final_odp):
        today = datetime.now()
        strname = today.strftime("%Y%m%d%H%M%S")
        filename = f'data\RFS_UPDATESTP_{strname}.csv'
        with open(filename, 'w', newline='') as f:
            #thewriter = csv.writer(f, delimiter='|') #without quotes
            #f.write('"SERVICE_NAME|SERVICE_NUMBER|ODP_PANEL|PORT_NAME   "\n') #quotes per line
            thewriter = csv.writer(f, quotechar='"', delimiter='|', quoting=csv.QUOTE_ALL, skipinitialspace=True) #quotes per cloumn
            thewriter.writerow(['SERVICE_NAME','SERVICE_NUMBER','ODP_PANEL','PORT_NAME'])
            if len(length_services) == 2:
                thewriter.writerow([f'{splitstring2}, {splitstring1}',f'{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
            elif len(length_services) == 1:
                if self._service[0] == '3':
                    thewriter.writerow([f'{splitstring1}',f'0{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
                else:
                    thewriter.writerow([f'{splitstring1}',f'{self._service}',f'{final_odp}',f'{final_odp}-{self._port}'])
        


    def letsinput(self):
        try:
            self._driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/omzetAccessNetwork')
            self._driver.find_element_by_id("servid").clear()
            if self._service[0] == '3':
                self._driver.find_element_by_id("servid").send_keys(f"0{self._service}")
            else:
                self._driver.find_element_by_id("servid").send_keys(self._service)
            self._driver.find_element_by_id("servid").send_keys(Keys.ENTER)

            time.sleep(3)

            length_services = self._driver.find_elements_by_name("selecteds")
            if len(length_services) == 2:
                sf1 = self._driver.find_element_by_id("tdserviceinfo1").text
                splitstring1 = sf1.split()[0]
                sf2 = self._driver.find_element_by_id("tdserviceinfo2").text
                splitstring2 = sf2.split()[0]
            elif len(length_services) == 1:
                sf1 = self._driver.find_element_by_id("tdserviceinfo1").text
                splitstring1 = sf1.split()[0]
                splitstring2 = None
        
            time.sleep(1)

        # go to odp
            self._driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint')
            time.sleep(2)
            self._driver.find_elements_by_id("filter")[5].click()
            self._driver.find_elements_by_id("deviceLocation")[0].send_keys(self._odp)
            self._driver.find_elements_by_id("deviceLocation")[0].send_keys(Keys.ENTER)
            time.sleep(1)
            
            elements = self._driver.find_elements_by_css_selector("td.column_number a")[0].text
            self._driver.find_element_by_link_text(f"{elements}").click()
            # elm = self._driver.find_elements_by_css_selector("td.expand")[0].text
            time.sleep(1)
            odp_name = self._driver.find_elements_by_class_name("label")[3]
            if elements == "16":
                txt = odp_name.text
                final_odp = txt.split('|', 1)[1]
            else:
                final_odp = odp_name.text
            self.createfile(length_services, splitstring1, splitstring2, final_odp)
        except:
            pass
        
