import streamlit as web
import functions

todos = functions.get_todo()

def add_todo():
    todo = web.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

web.title("Todo App")
web.write("Start your day with schedule")

for index, todo in enumerate(todos):
    checkbox = web.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del web.session_state[todo]
        web.rerun()

web.text_input(label="",placeholder="Add a new todo...",
               on_change=add_todo,key="new_todo")