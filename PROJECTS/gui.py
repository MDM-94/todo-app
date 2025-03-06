from idlelib.run import exit_now

import functions
import FreeSimpleGUI as FSG
import time
FSG.theme("DarkPurple3")

clock = FSG.Text("", key="clock")
label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter a todo", key='todo')
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")
exit_button = FSG.Button("Exit")


window = FSG.Window('My Todo app',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))



while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                FSG.popup("Please select an item first.", font=("Helvetica", 20))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                FSG.popup("Please select an item to complete first.", font=("Helvetica", 20))
        case "Exit":
            break



        case FSG.WIN_CLOSED:
            break



window.close()