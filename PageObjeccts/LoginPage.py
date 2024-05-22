from selenium.webdriver.common.by import By
class LoginPage:

    inputTxt_email_id="input-email"
    inputTxt_password_id = "input-password"
    btn_Login_xpath="//input[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def doLogin(self,username,password):
        self.driver.find_element(By.ID,self.inputTxt_email_id).send_keys(username)
        self.driver.find_element(By.ID, self.inputTxt_password_id).send_keys(password)
        self.driver.find_element(By.XPATH, self.btn_Login_xpath).click()

