import random, os


def get_action(message):
    return input(message)

def pas_gen():
    lower = 'qwertyuiopasdfghjklzxcvbnm'
    upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers ='0123456789'
    symbols = '[]{}()*;/,._-'
    operation = get_action('Пароль содержит спец.символы Y/N \n')
    if operation == "Y" or "y":
        all = lower + upper + numbers + symbols
    elif operation == "N" or 'n':
        all = lower + upper + numbers
    else:
        print("выберите  да или нет")
        return
    length = int(input('введите длинну пароля:\n'))
    password = "".join(random.sample(all, length))
    print(password + '\n\n')


if __name__ == "__main__":
    pas_gen() 