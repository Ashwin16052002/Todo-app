import functions

while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.get_todo()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            view=f"{index + 1}-{item}"
            print(view)

    elif user_input.startswith("edit"):

        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todo()


            edit_todo = input("Enter a new Todo: ")
            todos[number] = edit_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("You command is not valid")
            continue

    elif user_input.startswith("complete"):
            
        try:
            number = int(user_input[9:])

            todos = functions.get_todo()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
                
            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed successfully! "
            print(message)

        except IndexError:
            print("There is no Todo with that number")
            continue
        
    elif user_input.startswith("exit"):
        break

    else:
        print('Invalid command')

print("Bye!")

