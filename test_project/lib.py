def try_me():
    name = input("Hey bro, what's your name? \n")
    response = input(f'Nice to meet you {name}, do you want to be my friend? \n [Y/N]\n')
    if response.lower() == 'y':
        print('Cool !')
    elif response.lower() == 'n':
        print('Go fuck yourself then !')
    print("hum, I am sorry, I don't speak your language")