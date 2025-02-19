import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter a todo", key='todo')
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = FSG.Button("Edit")


window = FSG.Window('My Todo app',
                    layout=[[label], [input_box, add_button],
                            [list_box, edit_button]],
                    font=('Helvetica', 20))



while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case FSG.WIN_CLOSED:
            break



window.close()