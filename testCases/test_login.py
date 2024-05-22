from PageObjeccts.LoginPage import LoginPage
from PageObjeccts.AccountsPage import AccountsPage
import unittest


class Test_Login:
    baseURL = "https://naveenautomationlabs.com/opencart/index.php?route=account/login"

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.doLogin("jayantamandal122250@gmail.com","Wyndham@4099")
        self.ap=AccountsPage(self.driver)
        assert self.ap.isHeaderPresent()



