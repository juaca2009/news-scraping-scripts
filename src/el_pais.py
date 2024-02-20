from load_driver import load_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from load_data import add_rows_csv
from model.new import New

WAIT_TIME = 30
NUMER_OF_ITERATIONS = 150
MORE_NEWS_BUTTON_CLASS = ".mx-auto.w-64.bg-primary.px-8.py-2.text-2xl.font-bold.text-white.lg\\:bg-black.lg\\:hover\\:bg-primary"
ARTICLES_CLASS = ".hidden.lg\\:block"
JAVA_SCRIPT = "arguments[0].click();"

def get_articles(driver, type_new):
    for _ in range(NUMER_OF_ITERATIONS):
        WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.CSS_SELECTOR, MORE_NEWS_BUTTON_CLASS)))
        enlace_mas_contenido = driver.find_element(By.CSS_SELECTOR, MORE_NEWS_BUTTON_CLASS)
        driver.execute_script(JAVA_SCRIPT, enlace_mas_contenido)
        driver.implicitly_wait(5)
    articles = driver.find_elements(By.CSS_SELECTOR, ARTICLES_CLASS)
    new_objects = []
    for i in articles:
        title = get_etiquetas(i)
        if title != None:
            new_instance = New(None, title, type_new)
            new_objects.append(new_instance)
    add_rows_csv(new_objects)

def get_etiquetas(article):
    try:
        titles = article.find_elements(By.TAG_NAME, "h2")
        title = titles[0]
        return title.text
    except IndexError:
        pass

def home_button(driver):
    home_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/div/div[2]/a")
    driver.execute_script(JAVA_SCRIPT, home_button)

def get_politica(driver):
    politica_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[5]/div/ul/li[2]/ul/li[2]/a")
    driver.execute_script(JAVA_SCRIPT, politica_button)
    get_articles(driver, "Politica")
    home_button(driver)

def get_deportes(driver):
    deportes_button = driver.find_element(By.XPATH, '//a[@href="/deportes/"]')
    driver.execute_script(JAVA_SCRIPT, deportes_button)
    get_articles(driver, "Deportes")
    home_button(driver)

def get_tecnologia(driver):
    tecnologia_button = driver.find_element(By.XPATH, '//a[@href="/tecnologia/"]')
    driver.execute_script(JAVA_SCRIPT, tecnologia_button)
    get_articles(driver, "Tecnologia")
    home_button(driver)

if __name__ == "__main__":
    driver = load_driver()
    driver.get('https://www.elpais.com.co/')

    #get_politica(driver)
    #get_deportes(driver)
    get_tecnologia(driver)