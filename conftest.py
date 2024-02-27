import pytest
from playwright.sync_api import sync_playwright

from utils.logs import logger


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        logger.info("Launch browser")
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
