from selenium.webdriver import Keys
from seleniumpagefactory.Pagefactory import PageFactory
from pyshadow.main import Shadow


class Login(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login_link': ('ID', "sign_in"),
        'email_field': ('ID', "user_email"),
        'password_field': ('ID', "user_password"),
        'login_button': ('NAME', "commit"),
        'login_alert': ('CLASS_NAME', "alert.alert-warning"),
        'email_shadow_field': ('CSS', "div[contenteditable=\"plaintext-only\"]")
    }

    def access_login_page_through_link(self):
        self.login_link.click()

    def perform_login(self, email, password):
        self.email_field.set_text(email)
        self.password_field.set_text(password)
        self.login_button.click()
