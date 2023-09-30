from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def base(request):
    return render(request, "base.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('app')
        else:
            messages.info(request, "Invalid Credential")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, "Password not matching")
            return redirect('/')
        return redirect('login')
    return render(request, "register.html")


def app(request):
    return render(request, "app.html")


def end(request):
    return render(request, "end.html")
