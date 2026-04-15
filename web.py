import streamlit as web
import functions

todos = functions.get_todo()

web.title("Todo App")
web.write("Start your day with schedule")

for todo in todos:
    web.checkbox(todo)

web.text_input(label="",placeholder="Add a new todo...")