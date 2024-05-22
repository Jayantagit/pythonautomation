from selenium.webdriver.common.by import By


class AccountsPage:
    label_myaccount_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def isHeaderPresent(self):
        try:
             return self.driver.find_element(By.XPATH, self.label_myaccount_xpath).is_displayed()
        except:
            return False
