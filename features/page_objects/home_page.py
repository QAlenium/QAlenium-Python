from seleniumpagefactory import PageFactory


class Home(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.name = self.welcome_name.get_text()

    locators = {
        'my_tasks_menu_item': ('ID', "my_task"),
        'welcome_name': ('XPATH', "/html/body/div[1]/div[1]/div/div[2]/ul[2]/li[1]/a")
    }

    def get_my_tasks_menu_item(self, text):
        assert self.my_tasks_menu_item.is_displayed()
        assert self.my_tasks_menu_item.get_text() == text

    def access_my_tasks(self, text):
        self.get_my_tasks_menu_item(text)
        self.my_tasks_menu_item.click()

    def get_name_from_title(self):
        return self.welcome_name.get_text()