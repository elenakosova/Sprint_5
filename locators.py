from selenium.webdriver.common.by import By

class TestLocators:

    # Кнопка «Личный кабинет» на главной странице
    button_personal_account = By.XPATH, "//p[text()='Личный Кабинет']"

    # Кнопка «Войти в аккаунт» на главной странице
    button_log_in_account = By.XPATH, "//button[text()='Войти в аккаунт']"

    # Инпут Email на страницах Входа и регистрации
    input_email = By.XPATH, "//label[text()='Email']/../input"

    # Инпут Пароль на страницах Входа и регистрации
    input_password = By.XPATH, "//label[text()='Пароль']/../input"

    # Инпут Логин в личном кабинете
    input_login_personal_account = By.XPATH, "//label[text()='Логин']/../input"

    # Инпут Логин на странице Входа
    input_name = By.XPATH, "//label[text()='Имя']/../input"

    # Кнопка «Войти» на странице Входа
    button_log_in = By.XPATH, "//button[text()='Войти']"

    # Кнопка «Зарегистрироваться» на странице регистрации
    button_register = By.XPATH, "//button[text()='Зарегистрироваться']"

    # Нотификция «Некорректный пароль» под инпутом на странице Входа
    error_field_password = By.XPATH, "//form//fieldset[3]//p[text()='Некорректный пароль']"

    # Кнопка «Оформитье заказ» на главной странице
    button_set_an_order = By.XPATH, "//button[text()='Оформить заказ']"

    # Пункт меню «Выход» в личном кабинете
    menu_item_log_in = By.XPATH, "//button[text()='Выход']"

    # Ccылка «Войти» на странице регистрации  и восстановления пароля
    link_log_in = By.XPATH, "//a[text()='Войти']"

    # Заголовок «Вход» на странице авторизации
    header_log_in_page = By.XPATH, "//h2[text()='Вход']"

    # Пункт меню «Профиль» в личном кабинете
    menu_item_profile = By.XPATH, "//a[text()='Профиль']"

    # Пункт меню «Конструтор» в шапке сайта
    main_header_constructor = By.XPATH, "//p[text()='Конструктор']"

    # Заголовок раздела «Конструтор»
    header_constructor = By.XPATH, "//h1[text()='Соберите бургер']"

    # Логотип сайта
    logo_main_page = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"

    # Раздел «Соусы» в Конструкторе
    sauce_constructor = By.XPATH, "//span[text()='Соусы']"

    # Заголовок раздела «Соусы» в Конструкторе
    header_sauce_constructor = By.XPATH, "//h2[text()='Соусы']"

    # Раздел «Начинки» в Конструкторе
    filling_constructor = By.XPATH, "//span[text()='Начинки']"

    # Заголовок раздела «Начинки» в Конструкторе
    header_filling_constructor = By.XPATH, "//h2[text()='Начинки']"

    # Раздел «Булки» в Конструкторе
    bread_constructor = By.XPATH, "//span[text()='Булки']"

    # Заголовок раздела «Булки» в Конструкторе
    header_bread_constructor = By.XPATH, "//h2[text()='Булки']"

    # Выбранный таб в конструкторе
    select_tab_constructor = By.XPATH, ".//div[contains(@class, 'current')]/span"