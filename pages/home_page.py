from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.locators.locators_home import HomeLocators


class HomePage(BasePage):
    URL = 'https://automationintesting.online/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.button_let_me = page.locator(HomeLocators.BUTTON_LET_ME)
        self.input_name = page.locator(HomeLocators.USER_NAME_INPUT)
        self.input_email = page.locator(HomeLocators.EMAIL_INPUT)
        self.input_phone = page.locator(HomeLocators.PHONE_INPUT)
        self.input_subject = page.locator(HomeLocators.SUBJECT_INPUT)
        self.input_message = page.locator(HomeLocators.MESSAGE_INPUT)
        self.text_success = page.locator(HomeLocators.TEXT_SEND_SUCCESS)
        self.button_submit = page.locator(HomeLocators.BUTTON_SUBMIT)
        self.text_error_subject = page.locator(HomeLocators.TEXT_ERROR_SUBJECT)
        self.text_error_phone = page.locator(HomeLocators.TEXT_ERROR_PHONE)
        self.navigate_to_home_page()

    def send_message(self, name, email, phone, subject, message):
        self.button_let_me.click()
        self.input_name.fill(name)
        self.input_email.fill(email)
        self.input_phone.fill(phone)
        self.input_subject.fill(subject)
        self.input_message.fill(message)
        self.button_submit.click()

    def get_text(self):
        return self.text_success.inner_text()

    def get_text_error_subject(self):
        return self.text_error_subject.inner_text()

    def get_text_error_phone(self):
        return self.text_error_phone.inner_text()

    def navigate_to_home_page(self):
        """
        Método para navegar a la URL de la página de inicio.
        """
        self.page.goto(self.URL)
