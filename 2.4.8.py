from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Шаг 1: Ожидание, пока цена станет 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Шаг 2: Находим кнопку "Book" и кликаем
    book_button = browser.find_element(By.CSS_SELECTOR, "button#book")
    book_button.click()

    # Шаг 3: Прокручиваем страницу вниз
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Шаг 4: Берем X, считаем по формуле
    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value"))
    )
    x = x_element.text
    y = calc(x)
    print(f"Calculated answer: {y}")  # Для отладки

    # Шаг 5: Вводим ответ
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.click()  # Устанавливаем фокус
    answer_input.send_keys(y)

    # Шаг 6: Находим кнопку отправки и нажимаем
    solve_button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    solve_button.click()

finally:
    # Задержка для просмотра результата
    time.sleep(36)

    # Закрытие драйвера
    browser.quit()
