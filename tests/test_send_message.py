from pages.home_page import HomePage
from utils.logs import logger


def test_send_message_web_success(browser):
    """Este test valida el mensaje de envío exitoso al completar los campos de forma correcta"""

    logger.info("Send message to web")
    with browser as b:
        page = b.new_page()
        home_page = HomePage(page)
        home_page.send_message(name="Juan Perez",
                               email="test@test.com",
                               phone="12345678901",
                               subject="Prueba de caracteres",
                               message="Prueba de caracteres, probando que happy path con 20 caracteres mínimo")

        logger.info("Validate message successfully")
        assert home_page.get_text() == "We'll get back to you about"


def test_send_message_web_error(browser):
    """Este test valida el mensaje de error al no cumplir con el número de caracteres de los input"""

    logger.info("Send message to web")
    with browser as b:
        page = b.new_page()
        home_page = HomePage(page)
        home_page.send_message(name="Juan Perez",
                               email="test@test.com",
                               phone="12345",
                               subject="QA",
                               message="Prueba de caracteres")

        logger.info("Validate message unsuccessfully")
        assert home_page.get_text_error_subject() == "Subject must be between 5 and 100 characters."
        assert home_page.get_text_error_phone() == "Phone must be between 11 and 21 characters."
