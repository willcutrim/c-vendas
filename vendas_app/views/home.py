from django.shortcuts import render

def home(request):
    return render(request, 'html/home.html')