from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.shortcuts import redirect, render, HttpResponse

def login(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)

        print(user, username, senha)
        if user:
            login_django(request, user)
            print('passou')
            return redirect('/')
        else:
            return HttpResponse('email ou senha invalida')

    return render(request, 'html/login.html', {'users': users})