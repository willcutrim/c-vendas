from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User


def registrar(request):
    
    

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.get(username=username)
        if user:
            return HttpResponse('ja existe esse corno!')


        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('/login')

    return render(request, 'html/register.html')