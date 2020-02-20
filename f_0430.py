import os
import csv
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys


class CheckBulk:
	def __init__(self, _driver, _hasil, _id):
		self._driver = _driver
		self._hasil = _hasil
		self._id = _id

	def checkstatus(self):
		time.sleep(2)
		self._driver.find_element_by_xpath("//input[@type='search']").send_keys("art.t")
		time.sleep(2)
		self._driver.find_element_by_xpath("//select[@name='datatable_tabletools_length']/option[text()='All']").click()
		time.sleep(1)
		self._driver.find_element_by_link_text(self._id).click()
		time.sleep(2)
		x = self._driver.find_elements_by_css_selector("td a")[10].text
		z = self._driver.find_elements_by_class_name("column_center")[93].text
		self._hasil.write(f"{x.split('|')[1]} {z}\n")
		time.sleep(1.5)
		self._driver.find_elements_by_css_selector("div.jarviswidget-ctrls a.jarviswidget-toggle-btn")[1].click()