from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import platform

def load_driver():
    if platform.system() == 'Windows':
        return webdriver.Firefox(service=Service('Drivers/windows/geckodriver.exe'))
    elif platform.system() == 'Linux':
        return webdriver.Firefox(service=Service('Drivers/Linux/geckodriver'))
    else:
        raise Exception('Unsupported platform')

driver = load_driver()