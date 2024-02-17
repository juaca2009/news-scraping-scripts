from load_driver import load_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from load_data import add_rows_csv
from model.new import New

WAIT_TIME = 10
MORE_NEWS_BUTTON_CLASS = "btn_mas-noticias-largo"
ARTICLE_TAG_NAME = "article"
NUMER_OF_ITERATIONS = 2

POLITICA_IDS = ["m389-1-390", "m989-1-990", "m1462-1-1463", "m1775-1-1776"]
DEPORTES_IDS = ["m1452-1-1453", "m1071-1-1072", "m867-1-868", "m355-1-356"]
TECNOSFERA_IDS = ["m1024-1-1025", "m1304-1-1305", "m1577-1-1578"]

def click_more_news_and_collect_articles(driver, element_id, type_new):
    boton = driver.find_element(By.ID, element_id)
    driver.execute_script("arguments[0].click();", boton)
    for _ in range(NUMER_OF_ITERATIONS):
        enlace_mas_noticias = WebDriverWait(driver, WAIT_TIME).until(
            EC.visibility_of_element_located((By.CLASS_NAME, MORE_NEWS_BUTTON_CLASS))
        )
        enlace_mas_noticias.click()
        driver.implicitly_wait(5)
    articles = driver.find_elements(By.TAG_NAME, ARTICLE_TAG_NAME)
    new_objects = []
    for i in articles:
        date = i.get_attribute("data-publicacion")
        title = i.get_attribute("data-name")
        new_instance = New(date, title, type_new)
        new_objects.append(new_instance)
    add_rows_csv(new_objects)
    driver.back()

def go_to_main_page(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/header/div[1]/div[1]/div[3]/div/a").click()

def get_politica(driver):
    driver.find_element(By.XPATH, "//li[@class='politica']/a").click()
    for element_id in POLITICA_IDS:
        click_more_news_and_collect_articles(driver, element_id, "Politica")
    go_to_main_page(driver)

def get_deportes(driver):
    driver.find_element(By.XPATH, "//li[@class='deportes']/a").click()
    for element_id in DEPORTES_IDS:
        click_more_news_and_collect_articles(driver, element_id, "Deportes")
    go_to_main_page(driver)

def get_tecnosfera(driver):
    driver.find_element(By.XPATH, "//li[@class='tecnosfera']/a").click()
    for element_id in TECNOSFERA_IDS:
        click_more_news_and_collect_articles(driver, element_id, "Tecnologia")
    go_to_main_page(driver)


if __name__ == "__main__":
    driver = load_driver()
    driver.get('https://www.eltiempo.com/')

    #get_politica(driver)
    #get_deportes(driver)
    get_tecnosfera(driver)