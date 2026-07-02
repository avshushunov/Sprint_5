from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPage, AdPage
from helpers import generate_email, value_password, generate_name_ad
from constants import URL

class TestCreateAdUnathorized:
    def test_create_ad_unathorized(self, driver):
        driver.get(URL.BASE_URL)
        driver.find_element(*AdPage.CREATE_AD_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AdPage.MODAL_TITLE)).is_displayed()

class TestCreateAdAuthorized:
    def test_create_ad_authorized(self, driver):
        driver.get(URL.BASE_URL)
        driver.find_element(*AuthPage.LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CONFIRM_PASSWORD_INPUT).send_keys(value_password())
        driver.find_element(*AuthPage.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPage.USER_NAME))
        driver.find_element(*AdPage.CREATE_AD_BUTTON).click()
        name_ad = generate_name_ad()
        driver.find_element(*AdPage.NAME_INPUT).send_keys(name_ad)
        driver.find_element(*AdPage.CATEGORY_DROPDOWN).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AdPage.CATEGORY_DROPDOWN_HOBBY))
        driver.find_element(*AdPage.CATEGORY_DROPDOWN_HOBBY).click()
        driver.find_element(*AdPage.CONDITION_RADIO).click()
        driver.find_element(*AdPage.CITY_DROPDOWN).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AdPage.CITY_DROPDOWN_KAZAN))
        driver.find_element(*AdPage.CITY_DROPDOWN_KAZAN).click()
        driver.find_element(*AdPage.DESCRIPTION_INPUT).send_keys("Описание объявления такое")
        driver.find_element(*AdPage.PRICE_INPUT).send_keys("999")
        driver.find_element(*AdPage.PUBLISH_BUTTON).click()
        driver.refresh()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((AuthPage.PROFILE_BUTTON)))
        driver.find_element(*AuthPage.PROFILE_BUTTON).click()   
        card = card = card = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AdPage.AD_CARD))
        description = card.find_element(*AdPage.AD_DESCRIPTION).text
        

        assert card.is_displayed(), f"Карточка объявления не найдена"
        assert description == f"{name_ad}", f"Текст описания другой: {description}"
