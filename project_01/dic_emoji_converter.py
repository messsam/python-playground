def welcome():
    print('Welcome abroad!')

def greet_user():
    print('Hi there!')
    welcome()

def greet_user_one(name):
    print(f'Hi {name}!')
    welcome()

def greet_user_two(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    welcome()

def convert(message):
    split = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "😞",
        ":')": "😂",
        ":'(": "😭"
    }
    for word in split:
        if word in (":)", ":(", ":')", ":'("):
            message = message.replace(word, emojis.get(word, word))
    return message

message = input(">")

print(convert(message))
greet_user_one('Mohand')
greet_user_two('Essam', last_name='Mohand')