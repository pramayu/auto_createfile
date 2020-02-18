import os
import csv
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys


class CheckBulk:
	def __init__(self, _driver, _id):
		self._driver = _driver
		self._id = _id

	def checkstatus(self):
		print(self._id)
