from load_driver import load_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WAIT_TIME = 30
NUMER_OF_ITERATIONS = 2
MORE_NEWS_BUTTON_CLASS = "styles__VerMas-sc-o51gjq-3"
JAVA_SCRIPT = "arguments[0].click();"

def get_articles(driver):
    for _ in range(NUMER_OF_ITERATIONS):
        enlace_mas_contenido = WebDriverWait(driver, WAIT_TIME).until(
                EC.presence_of_element_located((By.CLASS_NAME, MORE_NEWS_BUTTON_CLASS))
            )
        driver.execute_script(JAVA_SCRIPT, enlace_mas_contenido)
        articles = driver.find_elements(By.CLASS_NAME, "grid-item")
        driver.implicitly_wait(5)
    return articles

def home_button(driver):
    home_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/div[4]/div/div[1]/div[1]/div[2]/a") 
    driver.execute_script(JAVA_SCRIPT, home_button)

def get_politica(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/"+
                    "div[4]/div/div[1]/div[3]/nav/a[7]").click() # Politica button
    articles = get_articles(driver)
    home_button(driver)

def get_deportes(driver):
    deportes_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/div[4]/div/div[3]/div/div/div/div[1]/a[6]")
    driver.execute_script(JAVA_SCRIPT, deportes_button)
    articles = get_articles(driver)
    home_button(driver)

def get_tecnologia(driver):
    tecnologia_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/div[4]/div/div[3]/div/div/div/div[1]/a[1]")
    driver.execute_script(JAVA_SCRIPT, tecnologia_button)
    articles = get_articles(driver)
    home_button(driver)

if __name__ == "__main__":
    driver = load_driver()
    driver.get('https://www.semana.com/')
    #get_politica(driver)
    #get_deportes(driver)
    get_tecnologia(driver)
