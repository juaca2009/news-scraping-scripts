from load_driver import load_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 30
NUMER_OF_ITERATIONS = 2
MORE_NEWS_BUTTON_CLASS = "styles__VerMas-sc-o51gjq-3"

driver = load_driver()
driver.get('https://www.semana.com/')

driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[7]/"+
                    "div[4]/div/div[1]/div[3]/nav/a[7]").click()

for i in range(NUMER_OF_ITERATIONS):
    enlace_mas_contenido = WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.CLASS_NAME, MORE_NEWS_BUTTON_CLASS))
        )
    driver.execute_script("arguments[0].click();", enlace_mas_contenido)
    articles = driver.find_elements(By.CLASS_NAME, "grid-item")
    driver.implicitly_wait(5)


print(len(articles))

