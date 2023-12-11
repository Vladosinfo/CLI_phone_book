import sys

# LISTENER = True
contacts_book = {}

MESSAGES = {
    "hello": "How can I help you?",
    "good_bye": "Good bye!",
    "close": "Good bye!",
    "exit": "Good bye!",
    "add": "Your contact has been saved",
    "change": "Your contact has been changed",
    "phone": "It's your phone number",
    "show_all": "These are all contacts"
}

COMMANDS = {
    "good_bye": MESSAGES["good_bye"],
    "close": MESSAGES["close"],
    "exit": MESSAGES["exit"],
    "hello": MESSAGES["hello"],
    "add": MESSAGES["add"],
    "change": MESSAGES["change"],
    "phone": MESSAGES["phone"],
    "show_all": MESSAGES["show_all"]
}

EXIT_COMMANDS = ["good_bye", "close", "exit"]

def message(mes):
    print(mes)

def exit(mes):
    print(mes)
    # LISTENER = False
    return False

command_handlers = {
    "good_bye": exit,
    "close": exit,
    "exit": exit,
    "hello": message,
    "add": "",
    "change": "",
    "phone": "",
    "show all": ""
}


def get_handler_command(com):
    return command_handlers[com]


def command_handler(com):
    handler = get_handler_command(com)
    handler(MESSAGES[com])


def parsing(user_input):
    commands = user_input.split(" ")
    # print(commands)
    # print(commands[0])
    if commands[0] in command_handlers:
        return commands[0]
    elif commands[0] == "good":
        if len(commands) > 1: 
            command = commands[0] + "_" + commands[1]
            return command 
        # else:
        #     print ("no")
    else:
        return "Err"


def question_answer():
    pass

def main():
    listener = True
    while listener == True:
        user_input = input("Input command >>> ")
        # print(user_input)
        command = parsing(user_input.lower())
        if command in EXIT_COMMANDS:
            listener = command_handler(command)
        else:
        # if command != "Err":
            print(f'command: {command}')
            command_handler(command)
        # else:
        #     listener = False
        

if __name__ == "__main__":
    main()



#### Бот повинен перебувати в безкінечному циклі, чекаючи команди користувача.
#### Бот завершує свою роботу, якщо зустрічає слова: .
#### Бот не чутливий до регістру введених команд.
# Бот приймає команди:
## "hello", відповідає у консоль "How can I help you?"
## "add ...". За цією командою бот зберігає у пам"яті (у словнику наприклад) новий контакт. Замість ... користувач вводить ім"я та номер телефону, обов"язково через пробіл.
## "change ..." За цією командою бот зберігає в пам"яті новий номер телефону існуючого контакту. Замість ... користувач вводить ім"я та номер телефону, обов"язково через пробіл.
## "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... користувач вводить ім"я контакту, чий номер треба показати.
## "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
## "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень виду "Enter user name", "Give me name and phone please" і т.п. Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
# Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
# Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.    