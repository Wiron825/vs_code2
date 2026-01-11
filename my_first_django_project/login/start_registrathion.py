import json
from random import randint
from new_user_bd import *
from old_user_bd import *

def check_password(password: str):
    flag = True
    if not ((13 > len(password) and len(password) >= 5) and (not password.isdigit()) and (not password.isalpha()) and ' ' not in password):
        flag = False
    elif len(set(password)) <= 2 or password == password[::-1]:
        flag = False
    return flag

def check_username(username: str):
    flag = True
    if not ((13 > len(username) and len(username) >= 2) and (not username.isdigit()) and username.count(' ') < 4):
        flag = False
    elif len(set(username)) <= 2:
        flag = False
    return flag

def registrathion(*args):
    total = {'result': ''}
    if len(args) == 3:
        username, email, password = args
        print("Имя:", username)
        print("type(Имя):", type(username))
        print("Пароль:", email)
        print("Код:", password)
        if username != '' and email != '' and password != '': 
            if not check_password(password=password):
                total = {'result': 'Пароль слишком простой, придумайте другой пароль'}
            elif not check_username(username=username):
                total = {'result': 'Ваш никнем не рабочий, придумайте другй никнейм'}
            else:
                # with open('data.csv', 'r', encoding='utf-8') as fl:
                #     data = [i.strip() for i in fl.readlines()]
                #     id = int(data[-1].split(',')[-1]) + 1

                # with open('data.csv', 'a', encoding='utf-8') as fl:
                #     fl.write(f'\n{username},{email},{password},{id}')

                # with open('data.json', 'r', encoding='utf-8') as f:
                #     loaded = json.load(f)
                #     print(loaded, type(loaded))
                #     loaded['name'] = '   ' + username
                #     print(loaded)

                # with open('data.json', 'w', encoding='utf-8') as f:
                #     json.dump(loaded, f, ensure_ascii=False)
                look_bd_new_user()
                print(look_id_new_user())
                look_bd_new_user()
                new_person_new_user(id_user=0, name_user=username, email_user=email, password_user=password)

                total = {'result': 'Регистрация прошла успешно'}
        else:
            total = {'result': 'Заполните все поля'}
    elif len(args) == 2:
        email, password = args

        print("Email:", email)
        print("password:", password)
        # with open('data.csv') as fl:
        #     text = fl.readlines()
        #     text1 = [email, password]
        #     flag = False
        #     for i in text:
        #         test = i.split(',')[1:-1]
        #         test[-1] = test[-1].strip()
        #         print(f'{test} - {text1}')
        #         if test == text1:
        #             flag = True
        #             username = i.split(',')[0]
        #             id = int(i.split(',')[-1].strip())
        #             print(id)
        #     if flag:
        #         with open('data_old.csv', 'r', encoding='utf-8') as fl:
        #             data = [i.strip() for i in fl.readlines()]
        #             id = int(data[-1].split(',')[-1]) + 1
        #         total = {'result': 'Вы успешно зашли на аккаунт'}
        #         with open('data_old.csv', 'a', encoding='utf-8') as fl:
        #             fl.write(f'\n{email},{password},{id}')
        #         with open('data.json', 'r', encoding='utf-8') as f:
        #             loaded = json.load(f)
        #             print(loaded)
        #             loaded['name'] = '   ' + username
        #             print(loaded)
        #         with open('data.json', 'w', encoding='utf-8') as f:
        #             json.dump(loaded, f, ensure_ascii=False)
        #     else:
        #         total = {'result': 'Аккаунт не найден'}
        
        if look_user_in_bd(email_user=email, password_user=password) and email != '' and password != '':
            new_person_old_user(email_user=email, password_user=password)
            total = {'result': 'Вы успешно зашли на аккаунт'}
        else:
            total = {'result': 'Аккаунт не найден'}
        print(look_bd_old_user())
    return total 
