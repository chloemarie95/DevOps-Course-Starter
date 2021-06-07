from flask import Flask, render_template, request, redirect, url_for
import requests
import os 
from card import Card
from data.view_model import ViewModel
from flask_config import Config
from data.trello_items import Trello_service

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    with app.app_context():
        service = Trello_service()
        service.initiate()

    @app.route('/')
    def index():
        board_id = os.getenv('TRELLO_BOARD_ID')
        items_response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards',params={'key': os.getenv('TRELLO_KEY'),'token': os.getenv('TRELLO_TOKEN')})
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
        todo_title = request.form['text-input']
        items_response = requests.post(
            f'https://api.trello.com/1/cards',
            params={
                'key': os.getenv('TRELLO_KEY'), 
                'token': os.getenv('TRELLO_TOKEN'), 
                'name': todo_title, 
                'idList': os.getenv('TRELLO_TODO_ID')
            }
        )
        return redirect('/')

    @app.route('/complete-item', methods=['POST'])
    def complete_item():
        card_id = request.form['id']
        items_response = requests.put(
            f'https://api.trello.com/1/cards/{card_id}',
            params={
                'key': os.getenv('TRELLO_KEY'),  
                'token': os.getenv('TRELLO_TOKEN'),
                'idList': os.getenv('TRELLO_DONE_ID')
            }
        )
        return redirect('/')

    @app.route('/start-item', methods=['POST'])
    def start_item():
        card_id = request.form['id']
        items_response = requests.put(
            f'https://api.trello.com/1/cards/{card_id}',
            params={
                'key': os.getenv('TRELLO_KEY'),  
                'token': os.getenv('TRELLO_TOKEN'),
                'idList': os.getenv('TRELLO_DOING_ID')
            }
        )
        return redirect('/')

    if __name__ == '__main__':
        app.run(debug=True)

    return app
    
