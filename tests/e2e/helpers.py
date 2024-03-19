import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.safari.service import Service as SafariService


def get_drivers_for_existing_browsers() -> []:
    return_value = []
    if os.path.exists('/applications/google chrome.app'):
        return_value.append(webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())))
    if os.path.exists('/applications/safari.app'):
        # you may need to run once 'safaridriver --enable'
        return_value.append(webdriver.Safari(service=SafariService(service_args=['diagnose'])))
    return return_value


