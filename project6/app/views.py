from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        o1 = Data(name=name, pno=pno, email=email, add=add, un=un, pw=pw)
        o1.save()
        return HttpResponse('Done......')
    return render(request, 'register.html')


def home(request):
    users = Data.objects.all()
    d = {'users': users}
    return render(request, 'home.html', d)
    


def demo(request):
    # d = {'name': 'likith', 'pno':1222222222}
    users = Data.objects.all()
    d = {'users': users}
    return render(request, 'demo.html', d)


def login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        users = Data.objects.all()
        for user in users:
            if user.un == un:
                if user.pw == pw:
                    d = {'users': [user]}
                    return render(request, 'home.html', d)
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('user Not Found')
    return render(request, 'login.html')