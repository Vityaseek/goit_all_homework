contact = {}


def input_error(func):
    def inner(*args):
        try:
            if func.__name__ == "add_contact":
                if contact.get(args[0]) and args[1]:
                    print(
                        'This contact already exists, use the "change" function to change phone')
                    return
            return func(*args)
        except (ValueError, IndexError):
            print("Enter the argument for the command")
        except KeyError:
            print("This contact does not exist,"
                  "write correct contact to make changes or add a different name")
    return inner


@input_error
def add_contact(*args):
    if args[0].isdigit():
        print('Write your name in letters, not numbers.')
        return
    contact[args[0]] = args[1]
    print('Contact added')


@input_error
def change_contact(*args):
    if contact[args[0]]:
        contact[args[0]] = args[1]
        print("Contact updated.")


@input_error
def show_phone(args: str):
    if contact[args[0]]:
        print(contact[args[0]])


def parser_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to parser bot! I have 5 general command: 'hello', 'add', 'change', 'show' and 'all'")
    while True:
        user_input = input('Enter a command:')
        command, *args = parser_input(user_input)

        if command in ['exit', 'close']:
            print('Good bey')
            break
        elif command == "hello":
            print('How can i help you')
        elif command == 'add':
            add_contact(*args)
        elif command == 'change':
            change_contact(*args)
        elif command == 'show':
            show_phone(args)
        elif command == "all":
            print(contact)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
