from selenium.webdriver.common.by import By


class AccountsPage:
    label_myaccount_xpath = "//h2[text()='My Account']"
    link_logout_linktext="Logout"
    link_login_linktext="Login"

    def __init__(self, driver):
        self.driver = driver

    def isHeaderPresent(self):
        try:
             return self.driver.find_element(By.XPATH, self.label_myaccount_xpath).is_displayed()
        except:
            return False
    def clickOnLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def clickOnLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()
