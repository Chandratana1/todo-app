from functions import get_todos, write_todos
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add/new, show, edit,complete or exit:")
    user_action = user_action.strip()
   # match user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]

# using with context manager
        todos = get_todos()

        todos.append(todo + '\n')


# using with context manager to read the file
        write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # new_todos = []
       # for item in todos:
          #  new_item = item.strip('\n')
          #  new_todos.append(new_item)
        #   print(new_todos)
      #  print(todos)
        # or
        #   list comprehension
        #   new_todos = [item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"

            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            #print(number)
            number = number -1
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            #print(existing_todos)

            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("You Entered Invalid Command")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:] )
            print(number)
            todos = get_todos()

            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Index is not available")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print(" Bye")