from function import register, login
from todo_function import new_task, delete_task, change_task

user_id = 0

k = int(input('Sign up/Sign in (0/1)'))
if k == 0:
    registered = register()
    if registered:
        print('Successfully registered')
        user_id = registered
    else:
        print('Registration failed')

if k == 1:
    user_id = login()
    if user_id != 0:
        print('Welcome')
    else:
        print('username or password incorrect')

if user_id != 0:
    n = int(input('Add new task/delete task/change task  (0/1/2)'))
    if n == 0:
        new_task(user_id)
    if n == 1:
        delete_task(user_id)
    if n == 2:
        change_task(user_id)
