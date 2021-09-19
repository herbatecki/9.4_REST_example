import json

class Todos:
    def __init__(self):
        try:
            with open("todos.json", 'r') as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos
    
    def get(self, id):
        todo  = [todo for todo in self.all() if todo['id']== id]
        if todo:
            return todo[0]
        return []

    def create(self, data):
        # data.pop('csrf_token') # niepotrzebne w aplickaji bez HTML
        self.todos.append(data) # co jeśli "data" nie będzie słownikiem? należałoby tu jakiś warunek dodać
        self.save_all()

    def save_all(self):
        with open('todos.json', 'w') as f:
            json.dump(self.todos, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

todos = Todos()