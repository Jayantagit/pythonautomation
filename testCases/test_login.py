import logging
import os.path

import pytest

from PageObjeccts.LoginPage import LoginPage
from PageObjeccts.AccountsPage import AccountsPage
import unittest
from Utilities.readProperties import ConfigReader
from Utilities.CustomLogger import CustomLogs


class Test_Login:
    baseURL = "https://naveenautomationlabs.com/opencart/index.php?route=account/login"

    log = CustomLogs.logger()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.ap=self.lp.doLogin(ConfigReader.readConfig("email"),ConfigReader.readConfig("password"))
        #self.ap=AccountsPage(self.driver)
        if self.ap.isHeaderPresent():
            self.log.info("Login success..")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            self.log.info("Login fail..")
            self.driver.close()
            assert False



