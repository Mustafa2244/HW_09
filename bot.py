telephone_book = []


def input_error(func):
    def decorator_with_arguments(command=""):
        try:
            res = func(command)
            if res is None:
                return "Phone not found"
        except KeyError:
            return "KeyError"
        except ValueError:
            return "Phone not number"
        except IndexError:
            return "Give me name and phone please"
        return res
    return decorator_with_arguments


def hello():
    return "How can I help you?"


@input_error
def add(command):
    name = command.split(" ")[1]
    phone_number = command.split(" ")[2]
    telephone_book.append(
        {
            name: int(phone_number)
        }
    )
    return "Phone was successfully added"


@input_error
def change(command):
    for user in telephone_book:
        if list(user.keys())[0] == command.split(" ")[1]:
            user[list(user.keys())[0]] = int(command.split(" ")[2])
            return "Phone was successfully changed"


@input_error
def phone(command):
    for user in telephone_book:
        if list(user.keys())[0] == command.split(" ")[1]:
            return user[list(user.keys())[0]]


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
