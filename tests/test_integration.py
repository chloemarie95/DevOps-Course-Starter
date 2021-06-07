import pytest
from dotenv import find_dotenv, load_dotenv
from unittest.mock import patch, Mock
import os
import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def sample_trello_cards_response(): 
    return [
        {
            "id": "1",
            "name": "Test Todo name",
            "idList": os.getenv('TRELLO_TODO_ID')
        }
    ]

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')

    assert str(response.data).find("New Todo")

def mock_get_cards(url, params):
    if url == f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards":
        response = Mock()
        # sample_trello_cards_response should point to some test response data
        response.json.return_value = sample_trello_cards_response()
        return response
    return None

