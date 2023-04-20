telephone_book = []


def input_error(command_name):
    def decorator(func):
        def decorator_with_arguments(command=""):
            try:
                if command_name == "hello" or command_name == "show_all":
                    res = func()
                else:
                    res = func(command)
                    if not res:
                        return "I'm not found result. Please check the input"

                if command_name == "add" or command_name == "change":
                    if len(command.split(" ")) < 3:
                        return "Give me name and phone please"
                    elif len(command.split(" ")) > 3:
                        return "Too many arguments. Give me name and phone please"
                elif command_name == "phone":
                    if len(command.split(" ")) < 2:
                        return "Enter user name please"
                    elif len(command.split(" ")) > 3:
                        return "Too many arguments. Enter only user name please"

            except KeyError:
                return "KeyError"
            except ValueError:
                return "ValueError"
            except IndexError:
                return "IndexError"
            return res
        return decorator_with_arguments
    return decorator


@input_error("hello")
def hello():
    return "How can I help you?"


@input_error("add")
def add(command):
    name = command.split(" ")[1]
    phone_number = command.split(" ")[2]
    telephone_book.append(
        {
            name: int(phone_number)
        }
    )
    return "Phone was successfully added"


@input_error("change")
def change(command):
    for user in telephone_book:
        if list(user.keys())[0] == command.split(" ")[1]:
            user[list(user.keys())[0]] = int(command.split(" ")[2])
            return "Phone was successfully changed"


@input_error("phone")
def phone(command):
    for user in telephone_book:
        if list(user.keys())[0] == command.split(" ")[1]:
            return user[list(user.keys())[0]]


@input_error("show_all")
def show_all():
    result = []
    for user in telephone_book:
        result.append(f"{list(user.keys())[0]}: {user[list(user.keys())[0]]}")
    return "\n".join(result)


def main():
    while True:
        command = input().lower()
        if command == "hello":
            print(hello())
        elif command.split(" ")[0] == "add":
            print(add(command))
        elif command.split(" ")[0] == "change":
            print(change(command))
        elif command.split(" ")[0] == "phone":
            print(phone(command))
        elif command == "show all":
            print(show_all())
        elif command == "exit" or command == "close" or command == "good bye" or command == ".":
            print("Good bye!")
            return


if __name__ == '__main__':
    main()
