from todo_app.data.view_model import ViewModel 
from todo_app.data.todo_item import Item
import pytest

def test_view_model_show_todo_items():
    items = [
        Item(1, "New Todo", "To Do"),
        Item(2, "In Progress Todo", "Doing"),
        Item(3, "Completed", "Done"),
    ]
    view_model = ViewModel(items)

    todo_items = view_model.todo_items()

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "To Do"

def test_view_model_show_doing_items():
    items = [
        Item(1, "New Todo", "To Do"),
        Item(2, "In Progress Todo", "Doing"),
        Item(3, "Completed", "Done"),
    ]
    view_model = ViewModel(items)

    todo_items = view_model.doing_items()

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Doing"

def test_view_model_show_done_items():
    items = [
        Item(1, "New Todo", "To Do"),
        Item(2, "In Progress Todo", "Doing"),
        Item(3, "Completed", "Done"),
    ]
    view_model = ViewModel(items)

    todo_items = view_model.done_items()

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Done"

