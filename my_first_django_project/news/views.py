from django.shortcuts import render
import json

# Create your views here.

def news_home(request):
    with open('data.json', encoding='utf-8') as fl:
        result = json.load(fl)
    data = {'user_name': result['name']}
    return render(request, 'news/news_home.html', data)
