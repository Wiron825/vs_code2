from django.shortcuts import render
import json

# Create your views here.

def index(request):
    with open('data.json', encoding='utf-8') as fl:
        result = json.load(fl)
    data = {'user_name': result['name'], 'title': 'Главная страница', 'streets': '', 'mean': ''}
    if request.method == 'POST' and request.POST.get('street') != None and request.POST.get('street') != '':
        street = request.POST.get('street')
        with open('data_streets.json', encoding='utf-8') as fl:
            result = json.load(fl)
        if result.get(street, False) == False:
            data['streets'] = 'Улица не найдена'
        else:
            data['streets'] = street
            data['mean'] = round(sum(result[street]) / len(result[street]), 2)
        with open("test_data.json", "w", encoding='utf-8') as fl:
            json.dump(data, fl, ensure_ascii=False)
    elif request.method == 'POST' and request.POST.get('number_ball') != None:
        print(data['streets'])
        with open('test_data.json', encoding='utf-8') as fl:
            data = json.load(fl)
        ball = request.POST.get('ball')
        if ball != []:
            ball_street = list(map(int, request.POST.get('number_ball')))
        else:
            ball_street = [0]
        with open('data_streets.json', encoding='utf-8') as fl:
            result = json.load(fl)
        with open('data_streets.json', 'w', encoding='utf-8') as f:
            if result.get(data.get('streets')) != None:
                result[data.get('streets')] = result.get(data.get('streets')) + ball_street
            json.dump(result, f, ensure_ascii=False)
            print(result.get(data.get('streets')))
            data['mean'] = ''
    return render(request, 'main/index.html', data)

def about(request):
    with open('data.json', encoding='utf-8') as fl:
        result = json.load(fl)
    data = {'user_name': result['name']}
    return render(request, 'main/about.html', data)

def login(request):
    with open('data.json', encoding='utf-8') as fl:
        result = json.load(fl)
    data = {'user_name': result['name']}
    return render(request, 'main/login.html', data)
