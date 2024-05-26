import logging
import os.path

import pytest

from PageObjeccts.LoginPage import LoginPage
from PageObjeccts.AccountsPage import AccountsPage
import unittest
from Utilities.readProperties import ConfigReader
from Utilities.CustomLogger import CustomLogs
from Utilities import ExcelUtils

class Test_Login:
    log = CustomLogs.logger()
    path=os.path.abspath(os.curdir)+"\\testData\OpenCart-Testdata.xlsx"

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver=setup
        lst_status=[]
        self.driver.get(ConfigReader.readConfig("baseURI"))
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.rows=ExcelUtils.getRowCount(self.path,"creds")
        for r in range(2,self.rows+1):
           self.email=ExcelUtils.readData(self.path,"creds",r,1)
           self.password = ExcelUtils.readData(self.path, "creds", r, 2)
           self.exp = ExcelUtils.readData(self.path, "creds", r, 3)
           self.ap = self.lp.doLogin(self.email,self.password)
           self.acctHeader=self.ap.isHeaderPresent()
           if self.exp=="valid":
               if self.acctHeader:
                   lst_status.append("pass")
                   self.ap.clickOnLogout()
                   self.ap.clickOnLogin()
               else:
                   lst_status.append("fail")
           elif self.exp=="invalid":
               if self.acctHeader:
                   lst_status.append("fail")
                   self.ap.clickOnLogout()
                   self.ap.clickOnLogin()
               else:
                   lst_status.append("pass")
        if "fail" not in lst_status:
            assert True
        else:
            assert False
        self.driver.close()
