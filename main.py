import sys

contacts_book = {}

MESSAGES = {
    "hello": "How can I help you?",
    "good_bye": "Good bye!",
    "close": "Good bye!",
    "exit": "Good bye!",
    "add": "Your contact has been added",
    "change": "Your contact has been changed",
    "phone": "It's your phone number: ",
    "show_all": "These are all contacts:"
}
EXIT_COMMANDS = ["good_bye", "close", "exit"]
WARNING_MESSAGES = {
    "correct_command": "Enter correct command",
    "name": "Enter user name",
    "name_phone": "Give me name and phone please",
    "missing_name": "This name is missing in contact book",
    "contacts_book_empty": "Contacts book is empty yet."
}
RED = "\033[91m"
GREEN = "\033[92m"
BOLD = '\033[1m'
RESET = "\033[0m"


def message_notice(notice, color = None):
    color = color or GREEN
    print(f"{color} {notice} {RESET}")
    

def message_warging(warning):
    print(f"{RED} {warning} {RESET}")


def input_error(func):
    def wrapper(user_input):
        try:
            res = func(user_input)
            return res
        except KeyError as err:
            message_warging(f"Error: {err}")
            return False
        except ValueError as err:
            message_warging(f"Error: {err}")
            return False
        except IndexError as err:
            message_warging(f"Error: {err}")
            return False
    return wrapper


def message(mes):
    message_notice(MESSAGES[mes[0]])


def exit(mes):
    message_notice(MESSAGES[mes[0]])
    return False


@input_error
def add(com):
    if len(com) < 3:
        raise ValueError(WARNING_MESSAGES["name_phone"])      
    contacts_book[com[1]] = com[2]
    message_notice(MESSAGES[com[0]])


def contacts_book_fullness():
    if len(contacts_book) == 0:
        message_warging(WARNING_MESSAGES["contacts_book_empty"])
        return 0    


def presence_name(com):
    if contacts_book.get(com[1]) == None:
        message_warging(WARNING_MESSAGES["missing_name"])
    else: return True


def show_all(com):
    if contacts_book_fullness() == 0: return
    message_notice(MESSAGES[com[0]])
    for key, val in contacts_book.items():
        message_notice(f"Name: {key.capitalize()} | phone: {val}", BOLD)


@input_error
def phone(com):
    if contacts_book_fullness() == 0: return
    if len(com) < 2:
        raise ValueError(WARNING_MESSAGES["name"])
    if presence_name(com): 
        message_notice(f"{MESSAGES[com[0]]}{contacts_book[com[1]]}", BOLD)


@input_error
def change(com):
    if contacts_book_fullness() == 0: return
    if len(com) < 3:
        raise ValueError(WARNING_MESSAGES["name_phone"])
    if presence_name(com):
        contacts_book[com[1]] = com[2]
        message_notice(MESSAGES[com[0]])


command_handlers = {
    "good_bye": exit,
    "close": exit,
    "exit": exit,
    "hello": message,
    "add": add,
    "change": change,
    "phone": phone,
    "show_all": show_all
}


def get_handler_command(com):
    return command_handlers[com]


def command_handler(com):
    handler = get_handler_command(com[0])
    handler(com)


@input_error
def parsing(user_input):
    commands = user_input.split(" ")
    if commands[0] in command_handlers:
        return commands
    elif commands[0] == "good" or commands[0] == "show":
        if len(commands) > 1: 
            commands[0] = commands[0] + "_" + commands[1]
            return parsing(commands[0])
        else :
            raise ValueError(WARNING_MESSAGES["correct_command"])
    else:
        raise ValueError(WARNING_MESSAGES["correct_command"])


def main():
    listener = True
    while listener == True:
        user_input = input("Input command >>> ")
        command = parsing(user_input.lower())
        if command != False:
            if command[0] in EXIT_COMMANDS:
                listener = command_handler(command)
            else:
                command_handler(command)


if __name__ == "__main__":
    main()
