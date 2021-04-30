from flask import Flask, render_template, request, redirect, url_for
import requests
import os 
from card import Card
from data.view_model import ViewModel

def create_app():
    app = Flask(__name__)

    # Provide test data instead of trello. Add data on line 14
    @app.route('/')
    def index():
        board_id = os.getenv('TRELLO_BOARD_ID')
        board_key = os.getenv('TRELLO_KEY')
        board_token = os.getenv('TRELLO_TOKEN')

        items_response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards',params={'key': board_key,'token': board_token})
        items_list = items_response.json()
        
        cards = [] 
        for item in items_list:
            new_card = Card(item["id"], item["name"], item["idList"])
            cards.append(new_card)

        # change to view model class - unit test
        view_model = ViewModel(cards) 

        return render_template('index.html', view_model = view_model)


    @app.route('/items', methods=['POST'])
    def add_item():
        board_id = os.getenv('TRELLO_BOARD_ID')
        board_key = os.getenv('TRELLO_KEY')
        board_token = os.getenv('TRELLO_TOKEN')
        todo_title = request.form['text-input']
        items_response = requests.post(
            f'https://api.trello.com/1/cards',
            params={
                'key': board_key, 
                'token': board_token, 
                'name': todo_title, 
                'idList': os.getenv('TRELLO_TODO_ID')
            }
        )
        return redirect('/')

    @app.route('/complete-item', methods=['POST'])
    def complete_item():
        card_id = request.form['id']
        board_id = os.getenv('TRELLO_BOARD_ID')
        board_key = os.getenv('TRELLO_KEY')
        board_token = os.getenv('TRELLO_TOKEN')
        items_response = requests.put(
            f'https://api.trello.com/1/cards/{card_id}',
            params={
                'key': board_key, 
                'token': board_token,
                'idList': os.getenv('TRELLO_DONE_ID')
            }
        )
        return redirect('/')

    if __name__ == '__main__':
        app.run(debug=True)

    return app
    