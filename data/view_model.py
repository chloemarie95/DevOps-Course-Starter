from data.todo_item import Item
class ViewModel:
    def __init__(self, items):
        self._items = items

    def todo_items(self):
        output = []

        for item in self.items:
            if item.status == "To Do":
                output.append(item)

    @property 
    def items(self):
        return self._items


