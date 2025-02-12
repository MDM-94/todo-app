import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter a todo", key='todo')
add_button = FSG.Button("Add")


window = FSG.Window('My Todo app',
                    layout=[[label], [input_box, add_button]],

                    font=('Helvetica', 20))



while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FSG.WIN_CLOSED:
            break

window.close()