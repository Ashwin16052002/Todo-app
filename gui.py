import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-do")
input_box = gui.InputText(tooltip="Enter To-do")
button = gui.Button("Add")

window = gui.Window("To-Do App",layout=[[label],[input_box,button]])
window.read()
window.close()