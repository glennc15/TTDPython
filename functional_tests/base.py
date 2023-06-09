# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import os 

from .server_tools import reset_database

MAX_WAIT = 5


class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.staging_server = os.environ.get('STAGING_SERVER')
		if self.staging_server:
			self.live_server_url = 'http://' + self.staging_server
			reset_database(self.staging_server)
			
	def tearDown(self):
		self.browser.quit()


	def wait(fn):  
		def modified_fn(*args, **kwargs):  
			start_time = time.time()
			while True:  
				try:
					return fn(*args, **kwargs)  
				except (AssertionError, WebDriverException) as e:  
					if time.time() - start_time > MAX_WAIT:
						raise e
					time.sleep(0.5)
		return modified_fn



	@wait 
	def wait_for_row_in_list_table(self, row_text):
		table = self.browser.find_element(By.ID, "id_list_table")
		rows = table.find_elements(By.TAG_NAME, "tr")
		self.assertIn(row_text, [row.text for row in rows])

		
	@wait
	def wait_to_be_logged_in(self, email):
		self.browser.find_element_by_link_text('Log out')
		navbar = self.browser.find_element_by_css_selector('.navbar')
		self.assertIn(email, navbar.text)

	@wait
	def wait_to_be_logged_out(self, email):
		self.browser.find_element_by_name('email')
		navbar = self.browser.find_element_by_css_selector('.navbar')
		self.assertNotIn(email, navbar.text)


	@wait 
	def wait_for(self, fn):
		return fn()


	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')


	# def wait_for_row_in_list_table(self, row_text):
	# 	start_time = time.time()
	# 	while True:
	# 		try:
	# 			table = self.browser.find_element(By.ID, "id_list_table")
	# 			rows = table.find_elements(By.TAG_NAME, "tr")
	# 			self.assertIn(row_text, [row.text for row in rows])
	# 			return
	# 		except (AssertionError, WebDriverException) as e:
	# 			if time.time() - start_time > MAX_WAIT:
	# 				raise e
	# 			time.sleep(0.5)


	# def wait_for(self, fn):
	# 	start_time = time.time()
	# 	while True:
	# 		try:
	# 			return fn()

	# 		except (AssertionError, WebDriverException) as e:
	# 			if time.time() - start_time > MAX_WAIT:
	# 				raise e
	# 			time.sleep(0.5)


	# def wait_to_be_logged_in(self, email):
	# 	self.wait_for(
	# 		lambda: self.browser.find_element_by_link_text('Log out')
	# 	)
	# 	navbar = self.browser.find_element_by_css_selector('.navbar')
	# 	self.assertIn(email, navbar.text)


	# def wait_to_be_logged_out(self, email):
	# 	self.wait_for(
	# 		lambda: self.browser.find_element_by_name('email')
	# 	)
	# 	navbar = self.browser.find_element_by_css_selector('.navbar')
	# 	self.assertNotIn(email, navbar.text)






