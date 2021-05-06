from data.todo_item import Item
import requests
from flask import current_app as app 
import os 
class Trello_service(object):
    trello_lists = {}
    def get_auth_params(self):
        return { 'key': os.getenv('TRELLO_KEY'), 
                'token': os.getenv('TRELLO_TOKEN'),
                'list': os.getenv('TRELLO_BOARD_ID')}

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

    response = requests.get(url, params = params)
    boards = response.json()

def get_lists():
    """
    Fetches all lists for Trello board

    """
    params = build_params({'cards': 'open'})
    url = build_url('/boards/%s/lists' % app.config['TRELLO_BOARD_ID'])

    response = requests.get(url, params = params)
    lists = response.json()

def get_list_id(self, name):
        """
        Get a trello list id for a give name from the list of all lists.

        Returns:
            listId:  The identifier for a given name
        """
        for listId in self.trello_lists:
            trello_list = self.trello_lists[listId]
            if trello_list.name == name:
                return listId

def get_items():
    """
    Fetches all items cards from Trello

    """

    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards"
    params = build_params()

    response = requests.get(url, params)
    
    trello_card = response.json()

    items = []

    for card in trello_card:
        items.append(Item.fromTrelloCard(card))

    return items

