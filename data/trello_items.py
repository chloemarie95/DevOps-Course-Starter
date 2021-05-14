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

    def initiate(self):
            trello_config = self.get_auth_params()
            trello_key = trello_config ['key']
            trello_token = trello_config ['token']
            trello_default_board = trello_config ['list']

            self.TRELLO_CREDENTIALS = f"key={trello_key}&token={trello_token}"
            self.TRELLO_BOARD_ID = trello_default_board                

    def build_url(self, endpoint):
        return app.config['TRELLO_BASE_URL'] + endpoint

    def build_params(self, params = {}):
        full_params = self.get_auth_params()
        full_params.update(params)
        return full_params

    def get_boards(self):
        """
        Fetches all boards from Trello

        """
        params = self.build_params()
        url = self.build_url('/members/me/boards')

        response = requests.get(url, params = params)
        boards = response.json()

    def get_lists(self):
        """
        Fetches all lists for Trello board

        """
        params = self.build_params({'cards': 'open'})
        url = self.build_url('/boards/%s/lists' % app.config['TRELLO_BOARD_ID'])

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

    def get_items(self):
        """
        Fetches all items cards from Trello

        """

        url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards"
        params = self.build_params()

        response = requests.get(url, params)
        
        trello_card = response.json()

        items = []

        for card in trello_card:
            items.append(Item.fromTrelloCard(card))

        return items

