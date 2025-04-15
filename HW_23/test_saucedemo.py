"""
 Список последовательных инструкций:

1 Экран логина
Открыть https://www.saucedemo.com/
Ввести имя пользователя в поле: #user-name
Ввести пароль в поле: #password
Нажать кнопку "Login": #login-button

2 Главная страница
После успешного "Login" отображается страница с товарами: #inventory_container
Выбрать любой товар и нажать кнопку "Add to cart": #add-to-cart-sauce-labs-backpack
Проверить, что иконка корзины показывает "1": .shopping_cart_badge
Нажать на иконку корзины: .shopping_cart_link

3 Страница корзины
Проверить наличие добавленного товара: .cart_item
Нажать кнопку "Checkout": #checkout

4 Страница оформления заказа
После успешного перехода отображается страница оформления заказа: .checkout_info
Заполнить поля:
First name: #first-name
Last name: #last-name
Zip.Postal code: #postal-code
Нажать "Continue" кнопку: #continue

5 Страница подтверждения
Проверить информацию о заказе: .checkout_summary_container
Нажать "Finish": #finish

6 Страница завершения
После успешного перехода отображается страница завершения заказа: .checkout_complete_container
Проверить сообщение об успешном заказе: .complete-header
Нажать "Back Home" для возврата на главную: #back-to-products
"""
