import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_order_flow():
    browser = webdriver.Chrome()
    try:
        # 1 Экран логина
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()

        # 2 Главная страница
        inventory_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert inventory_container.is_displayed()
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1"
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 3 Страница корзины
        cart_item = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        assert cart_item.is_displayed()
        browser.find_element(By.ID, "checkout").click()

        # 4 Страница оформления заказа
        checkout_info = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout_info"))
        )
        assert checkout_info.is_displayed()
        browser.execute_script(
            "arguments[0].scrollIntoView();",
            browser.find_element(By.ID, "first-name")
        )
        browser.find_element(By.ID, "first-name").send_keys("John")
        browser.find_element(By.ID, "last-name").send_keys("Doe")
        browser.find_element(By.ID, "postal-code").send_keys("12345")
        browser.find_element(By.ID, "continue").click()

        # 5 Страница подтверждения
        summary_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout_summary_container"))
        )
        assert summary_container.is_displayed()
        browser.find_element(By.ID, "finish").click()

        # 6 Страница завершения
        complete_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout_complete_container"))
        )
        assert complete_container.is_displayed()
        complete_header = browser.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU" in complete_header.upper()
        browser.find_element(By.ID, "back-to-products").click()

    finally:
        time.sleep(2)
        browser.quit()
