from seleniumpagefactory import PageFactory
from features.page_objects.home_page import Home
import string
import random


class MyTasks(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'list_title': ('XPATH', "/html/body/div[1]/h1"),
        'task_field': ('ID', "new_task"),
        'add_button': ('CLASS_NAME', "input-group-addon.glyphicon.glyphicon-plus"),
        'task_entry': ('CLASS_NAME', "ng-scope"),
        'subtask_button': ('CLASS_NAME', "btn.btn-xs.btn-primary.ng-binding")
    }

    def validate_list_title(self, message):
        name = Home(self.driver).get_name_from_title().split(", ")[1].split("!")[0]
        final_message = message.replace("USERNAME", name)
        assert self.list_title.get_text() == final_message

    def add_new_task(self, task_name_size):
        task_name = self.generate_random_text(task_name_size)
        self.task_field.send_keys(task_name)
        self.add_button.click()

    def validate_task_was_not_created(self):
        assert not self.task_entry.is_displayed()

    def validate_task_was_created(self):
        assert self.task_entry.is_displayed()

    def access_subtask(self):
        assert "Manage Subtasks" in self.subtask_button.get_text()
        self.subtask_button.click()

    def validate_subtasks_count(self, number):
        assert self.subtask_button.text().contains(number)

    def generate_random_text(self, number_of_characters):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(number_of_characters))
