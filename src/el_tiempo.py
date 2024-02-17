from load_driver import load_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from model.new import new

WAIT_TIME = 10
MORE_NEWS_BUTTON_CLASS = "btn_mas-noticias-largo"
ARTICLE_TAG_NAME = "article"
NUMER_OF_ITERATIONS = 20

POLITICA_IDS = ["m389-1-390", " m989-1-990", "m1462-1-1463", "m1775-1-1776"]
DEPORTES_IDS = ["m1452-1-1453", "m1071-1-1072", "m1292-1-1293", "m1701-1-1702"]
TECNOSFERA_IDS = ["m1024-1-1025", "m1304-1-1305", "m1577-1-1578"]

def click_more_news_and_collect_articles(driver, element_id):
    driver.find_element(By.ID, element_id).click()
    for _ in range(NUMER_OF_ITERATIONS):
        enlace_mas_noticias = WebDriverWait(driver, WAIT_TIME).until(
            EC.visibility_of_element_located((By.CLASS_NAME, MORE_NEWS_BUTTON_CLASS))
        )
        enlace_mas_noticias.click()
        driver.implicitly_wait(5)
    articles = driver.find_elements(By.TAG_NAME, ARTICLE_TAG_NAME)
    driver.back()

def go_to_main_page(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/header/div[1]/div[1]/div[3]/div/a").click()

def get_politica(driver):
    driver.find_element(By.XPATH, "//li[@class='politica']/a").click()
    for element_id in POLITICA_IDS:
        click_more_news_and_collect_articles(driver, element_id)
    go_to_main_page(driver)

def get_deportes(driver):
    driver.find_element(By.XPATH, "//li[@class='deportes']/a").click()
    for element_id in DEPORTES_IDS:
        click_more_news_and_collect_articles(driver, element_id)
    go_to_main_page(driver)

def get_tecnosfera(driver):
    driver.find_element(By.XPATH, "//li[@class='tecnosfera']/a").click()
    for element_id in TECNOSFERA_IDS:
        click_more_news_and_collect_articles(driver, element_id)
    go_to_main_page(driver)


if __name__ == "__main__":
    driver = load_driver()
    driver.get('https://www.eltiempo.com/')

    #get_politica(driver)
    #get_deportes(driver)
    get_tecnosfera(driver)