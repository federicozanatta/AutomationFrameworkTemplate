from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_xpath = '//*[@id="navbarText"]/ul/li[3]/a'
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    def clicklogout(self):
        #self.driver.find_element("xpath", self.link_logout_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
