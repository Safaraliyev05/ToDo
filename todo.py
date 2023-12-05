import json
from datetime import datetime, timedelta


def get_data():
    try:
        with open('todo.json', 'r') as f:
            tasks = json.load(f)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        with open('todo.json', 'w') as f:
            json.dump([], f, indent=4)
            return []


class ToDoList:
    def __init__(self, text, expires_at, owner_id):
        self.text = text
        self.expires_at = expires_at
        self.owner_id = owner_id

    def add_task(self, owner_id):
        tasks = get_data()
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) != 0 else 1,
            'tasks': self.text,
            'expires_at': (datetime.now() + timedelta(hours=self.expires_at)).strftime("%Y-%m-%d %H:%M:%S"),
            'owner_id': owner_id
        }
        tasks.append(task)
        with open('todo.json', 'w') as f:
            json.dump(tasks, f, indent=4)

    def delete_task(self, task_id, owner_id):
        tasks = get_data()
        updated_tasks = [task for task in tasks if task['id'] != task_id or task['owner_id'] != owner_id]
        with open('todo.json', 'w') as f:
            json.dump(updated_tasks, f, indent=4)

    def change_task(self, task_id, new_text, new_duration, owner_id):
        tasks = get_data()
        for task in tasks:
            if task['id'] == task_id and task['owner_id'] == owner_id:
                task['tasks'] = new_text
                task['expires_at'] = (datetime.now() + timedelta(hours=new_duration)).strftime("%Y-%m-%d %H:%M")
                break
        with open('todo.json', 'w') as f:
            json.dump(tasks, f, indent=4)
