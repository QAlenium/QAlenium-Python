from behave import given, when, then

from features.page_objects.home_page import Home
from features.page_objects.login_page import Login
from features.page_objects.my_subtasks_page import MySubTasks
from features.page_objects.my_tasks_page import MyTasks
from helper import webdriver


@given('I have the endpoint "{endpoint_param}"')
def step_impl(context, endpoint_param):
    webdriver.open(context.helper_func, endpoint_param)


@given('I have the user email "{email_param}"')
def step_impl(context, email_param):
    context.email = email_param


@given('I have the user password "{password_param}"')
def step_impl(context, password_param):
    context.password = password_param


@then('I should be able to login')
def step_impl(context):
    login_page = Login(context.helper_func._driver)
    login_page.access_login_page_through_link()
    login_page.perform_login(context.email, context.password)


@given('I access the "{my_task}" menu')
def step_impl(context, my_task):
    context.home_page = Home(context.helper_func._driver)
    context.home_page.access_my_tasks(my_task)


@given('I can see "{message}"')
def step_impl(context, message):
    context.my_tasks_page = MyTasks(context.helper_func._driver)
    context.my_tasks_page.validate_list_title(message)


@when('I create a new task')
def step_impl(context):
    context.my_tasks_page.add_new_task(5)


@then('I can see the created task in the list')
def step_impl(context):
    context.my_tasks_page.validate_task_was_created()


@when('I try to create a new task with "{number}" characters')
def step_impl(context, number):
    context.my_tasks_page.add_new_task(number)


@then('I should not be able to create it')
def step_impl(context):
    context.my_tasks_page.validate_task_created()


@then('I should be able to create a new task')
def step_impl(context):
    context.home_page = Home(context.helper_func._driver)
    context.home_page.access_my_tasks("My Tasks")
    context.my_tasks_page = MyTasks(context.helper_func._driver)
    context.my_tasks_page.add_new_task(5)
    context.my_tasks_page.access_subtask()


@given('I create a subtask')
def step_impl(context):
    context.my_sub_tasks_page = MySubTasks(context.helper_func._driver)
    context.my_sub_tasks_page.add_sub_task()


@then('I can see the subtask created')
def step_impl(context):
    context.my_sub_tasks_page.validate_subtask_creation()
