from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helper.helper_base import HelperFunc


def before_scenario(context, scenario):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    context.helper_func = HelperFunc(driver)


def after_scenario(context, scenario):
    context.helper_func.close()
