from django.shortcuts import render
from django.http import HttpResponse
from login.start_registrathion import registrathion
import json
# Create your views here.

def new_login(request):
    total = {'result': ''}
    if request.method == 'POST' and request.POST.get('username') != None:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        total = registrathion(username, email, password)

        # return HttpResponse("Данные получены!")
    elif request.method == 'POST' and request.POST.get('username') == None:
        email = request.POST.get('old_email')
        password = request.POST.get('old_password')

        total = registrathion(email, password)

    return render(request, 'new_login/new_login.html', total)
