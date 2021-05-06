
# Time: 49:47
from data.todo_item import Item
import requests
from flask import current_app as app 
import os 

def get_auth_params():
    return { 
        'key': app.config['TRELLO_API_KEY'], 
        'token': app.config['TRELLO_API_SECRET']
        }

def build_url(endpoint):
    return app.config['TRELLO_BASE_URL'] + endpoint

def build_params(params = {}):
    full_params = get_auth_params()
    full_params.update(params)
    return full_params

def get_boards():
    """
    Fetches all boards from Trello

    """
    params = build_params()
    url = build_url('/members/me/boards')

    reponse = requests.get(url, params = params)
    boards = response.json()

def get_lists():
    """
    Fetches all lists for Trello board

    """
    params = build_params({'cards': 'open'})
    url = build_url('/boards/%s/lists' % app.config['TRELLO_BOARD_ID'])

    response = requests.get(url, params = params)
    lists = response.json()


def get_items():
    """
    Fetches all items cards from Trello

    """

    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards"
    params = build_params()

    response = requests.get(url, params)
    
    trello_card = response.json()

    items = []

    for card in trello_cards:
        items.append(Item.fromTrelloCard(card))

    return items

