from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPage
from helpers import generate_email, value_password
from constants import URL

class TestRegistration:
    def test_registration_successful(self, driver):
        driver.get(URL.BASE_URL)
        driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CONFIRM_PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.USER_NAME))
        assert driver.find_element(*AuthPage.USER_NAME).text == "User."
        assert driver.find_element(*AuthPage.AVATAR).is_displayed()

    
    def test_registration_email_incorrect_mask(self, driver):
        driver.get(URL.BASE_URL)
        driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys("email@test")
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CONFIRM_PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.ERROR_MESSAGE))  
        input_error = driver.find_elements(*AuthPage.INPUT_ERROR)
        error_text = driver.find_element(*AuthPage.ERROR_MESSAGE).text

        assert error_text == "Ошибка", f"Текст ошибки: {error_text}"
        assert len(input_error) == 3, f"Найдено {len(input_error)} полей с ошибкой, ожидается 3"
        for error in input_error:
            border_color = error.value_of_css_property("border-color")
            assert border_color == "rgb(255, 105, 114)", f"Цвет рамки: {border_color}"

    def test_registration_existing_user(self, driver):
        driver.get(URL.BASE_URL)
        driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.NO_ACCOUNT_BUTTON).click()
        email = generate_email()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(email)
        password = value_password()
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPage.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPage.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.USER_NAME))
        driver.find_element(*AuthPage.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.LOGIN_REGISTRATION_BUTTON))
        driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPage.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPage.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.ERROR_MESSAGE))
        input_error = driver.find_elements(*AuthPage.INPUT_ERROR)
        error_text = driver.find_element(*AuthPage.ERROR_MESSAGE).text

        assert error_text == "Ошибка", f"Текст ошибки: {error_text}"
        assert len(input_error) == 3, f"Найдено {len(input_error)} полей с ошибкой, ожидается 3"
        for error in input_error:
            border_color = error.value_of_css_property("border-color")
            assert border_color == "rgb(255, 105, 114)", f"Цвет рамки: {border_color}"