# -*- coding: utf-8 -*-
import os
import urlparse

from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
	BASE_URL = 'https://www.ok.ru'
	PATH = ''

	def __init__(self, driver):
		self.driver = driver

	def open(self):
		url = urlparse.urljoin(self.BASE_URL, self.PATH)
		self.driver.get(url)
		self.driver.maximize_window()


class Component(object):
	def __init__(self, driver):
		self.driver = driver


class AuthPage(Page):
	PATH = ''

	@property
	def form(self):
		return AuthForm(self.driver)

	@property
	def user_header(self):
		return UserHeader(self.driver)

	def login(self):
		user_login = 'technopark34'
		password = os.environ['OK_PASSWORD']

		auth_form = self.form
		auth_form.set_login(user_login)
		auth_form.set_password(password)
		auth_form.submit()

		return self.user_header.get_username()


class UserPage(Page):
	PATH = ''

	def login(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		return auth_page.login()


class AuthForm(Component):
	LOGIN = '//input[@id="field_email"]'
	PASSWORD = '//input[@id="field_password"]'
	LOGIN_BUTTON = '//input[@class="button-pro __wide"]'

	def set_login(self, login):
		self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

	def set_password(self, pwd):
		self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

	def submit(self):
		self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


class UserHeader(Component):
	USERNAME = '//h1[@class="mctc_name_tx bl"]'

	def get_username(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.USERNAME).text
		)
