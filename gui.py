import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-do")
input_box = gui.InputText(tooltip="Enter To-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todo(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window("To-Do App",
                    layout=[[label],
                            [input_box,add_button],
                            [list_box,edit_button,complete_button],
                            [exit_button]],
                    font=('helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todo()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=" ")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break
window.close()