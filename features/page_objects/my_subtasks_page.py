from seleniumpagefactory import PageFactory


class MySubTasks(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'subtask_title': ('CLASS_NAME', "modal-title ng-binding"),
        'subtask_description': ('ID', "edit_task"),
        'subtask_due_date': ('ID', "due_date"),
        'subtask_add_button': ('ID', "add-subtask"),
        'subtask_entry': ('CLASS_NAME', "ng-scope")
    }

    def validate_task_id(self):
        assert self.subtask_title.text().contains(type(int))

    def validate_task_description(self):
        assert self.subtask_description.is_displayed()

    def add_subtask_description(self, description):
        assert len(description) > 250
        self.subtask_description.send_keys(description)

    def add_subtask_due_date(self):
        assert self.subtask_due_date.is_displayed()

    def add_sub_task(self):
        self.subtask_add_button.click()

    def validate_subtask_creation(self):
        assert self.subtask_entry.is_displayed()
