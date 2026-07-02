from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPage
from helpers import generate_email, value_password
from constants import URL

class TestLogin:

    def test_login_successful(self, driver):
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
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.USER_NAME))
        user_name_text = driver.find_element(*AuthPage.USER_NAME).text
        avatar = driver.find_element(*AuthPage.AVATAR)
        
        assert user_name_text == "User."
        assert avatar.is_displayed()


class TestLogout:
    
    def test_logout_successful(self, driver):
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
        avatar_elements = driver.find_elements(*AuthPage.AVATAR)
        user_name_elements = driver.find_elements(*AuthPage.USER_NAME)
        login_button = driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON)
  
        assert len(avatar_elements) == 0, "Аватар всё ещё отображается"
        assert len(user_name_elements) == 0, "Имя User всё ещё отображается"
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не найдена"