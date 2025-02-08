import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter a todo")
add_button = FSG.Button("Add")


window = FSG.Window('My Todo app', layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()