def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_user_phonenumber(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def user_phonenuber(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact not found'

def all_users_and_numbers(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f'Name :{name}, Phone: {phone}\n'
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_user_phonenumber(args, contacts))
        elif command == "phone":
            print(user_phonenuber(args, contacts))
        elif command == "all":
            print(all_users_and_numbers(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()