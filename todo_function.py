from todo import ToDoList


def new_task(owner_id):
    text = input('Enter your task: ')
    expires_at = int(input('Enter duration in hours: '))

    task = ToDoList(text, expires_at, '')
    task.add_task(owner_id)
    print("Task added successfully!")


def delete_task(owner_id):
    task_id = int(input('Enter task id to delete: '))

    task = ToDoList('', '', '')
    task.delete_task(task_id, owner_id)
    print(f"Task with ID {task_id} deleted successfully!")


def change_task(owner_id):
    task_id = int(input('Enter task id to change: '))
    new_text = input('Enter new task text: ')
    new_duration = int(input('Enter new duration in hours: '))

    task = ToDoList('', '', '')
    task.change_task(task_id, new_text, new_duration, owner_id)
    print(f"Task with ID {task_id} updated successfully!")
