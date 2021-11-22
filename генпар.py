import random

def password_gen():
    symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
    spec = '[]{}()*;/,._-@#$%!^<>\/?"§±'
    while True:
        try:
            number_of_symbols = int(input('Please enter number of symbols in your password: '))
            break
        except:
            print('It is not digits, try again')
            continue
    while True:
        spec_symbols = input('Do you want special characters in the password (Y - yes, N - no): ')
        if spec_symbols == 'y':
            break
        elif spec_symbols == 'n':
            break
        else:
            print('Smth went wrong, try again please!')
            continue

    password = []

    for i in range(number_of_symbols):
        if spec_symbols.lower() == 'y':
            password.append(random.choice(symbols + spec))
        elif spec_symbols.lower() == 'n':
            password.append(random.choice(symbols))

    return ''.join(password)


if __name__ == '__main__':
    while True:
        k = input('If you want to generate password enter 1 if no enter exit: ')
        if k == '1':
            print(password_gen())
        elif k == 'exit':
            print('See you!')
            break
        else:
            print('Smth went wrong, try again please!')
            continue