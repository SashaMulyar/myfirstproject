import random

def generator():
    elements='1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
    symbols='!@#$%&*()_-+='
    while True:
        try:
            length=int(input('number of password elements: '))
            break
        except:
            print('input number')
            continue
    while True:
        symbols_in_password=input('symbols in the password? input yes or no: ')
        if symbols_in_password=='yes':
            password=''.join(random.sample(elements+symbols,length))
            break
        elif symbols_in_password=='no':
            password=''.join(random.sample(elements,length))
            break
        else:
            print('again')
            continue
    print(password)
if __name__ == "__main__":
    generator() 