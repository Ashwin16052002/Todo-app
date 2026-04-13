import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-do")
input_box = gui.InputText(tooltip="Enter To-do", key="Todo")
button = gui.Button("Add")

window = gui.Window("To-Do App",
                    layout=[[label],[input_box,button]],
                    font=('helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['Todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break

window.close()