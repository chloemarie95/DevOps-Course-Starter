import os

class Item:

    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod 
    def from_trello_card(cls, card):
        status = ""

        if card["idList"] == os.getenv("TRELLO_TODO_ID"):
            status = "To Do"
        elif card["idList"] == os.getenv("TRELLO_DOING_ID"):
            status = "Doing"
        elif card["idList"] == os.getenv("TRELLO_DONE_ID"):
            status = "Done"

        return cls(card['id'], card['name'], status)

    def reset(self):
        self.status = 'To Do'

    def start(self):
        self.status = 'Doing'

    def complete(self):
        self.status = 'Done' 