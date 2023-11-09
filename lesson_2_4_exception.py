import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    #нажимаем кнопку
    button = browser.find_element(By.ID, "book").click()

    # считываем х и рассчитываем значение функции
    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))

    # скроллим страницу и вводим значение функции
    input = browser.find_element(By.ID, "answer")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()