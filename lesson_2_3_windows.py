from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    #переключаемся на алерт и принимаем
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    # считывается значение х
    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))

    # вводим значение функции в поле
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)


    # нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
