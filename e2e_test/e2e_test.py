import os
from threading import Thread
import app
import pytest
from selenium  import webdriver
from dotenv import load_dotenv, find_dotenv
from data.trello_items import Trello_service
import time
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

@pytest.fixture(scope="module")
def test_app(driver):
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    service = Trello_service()
    service.initiate()
    board_id = os.environ['TRELLO_BOARD_ID']
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)
    service.delete_board(board_id)

def test_check_title(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

def test_add_item(driver):
    driver.get('http://localhost:5000/')
    text = "Test To Do Item-Selenium"
    
    titleInput = driver.find_element_by_id("title-input")
    titleInput.clear()
    titleInput.send_keys(text)
    driver.implicitly_wait(2)
    button = driver.find_element_by_id("add-button")
    button.click()
    
    assert text in driver.find_element_by_xpath("//ul").text