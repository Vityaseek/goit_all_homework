contact = {}


def add_contact(*args):
    try:
        if args[0].isdigit():
            print('Write your name in letters, not numbers.')
            return
        contact[args[0]] = args[1]
        print('Contact aded')
    except (IndexError, ValueError):
        print("Invalid input, you must enter your name and phone number")


def change_contact(*args):
    try:
        if contact.get(args[0]):
            contact[args[0]] = args[1]
            print("Contact updated.")
        else:
            print("This contact does not exist,"
                  "add a contact to make changes or enter a different name")
    except (IndexError, ValueError):
        print(
            "Invalid input, you must enter command and your name, and new phone for change")


def show_phone(args: str):
    try:
        if contact.get(args[0]):
            print(contact[args[0]])
        else:
            print("The name does not exist or the input is incorrect,"
                  "try entering the name with a capital letter")
    except (IndexError, ValueError):
        print("Invalid input, you must enter command and your name for show phone")


def show_all():
    print(contact)


def parser_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to parser bot")
    while True:
        user_input = input('write command:')
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
            show_all()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
