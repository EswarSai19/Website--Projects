from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        print("Data: ", request.POST)

        if password==password2:
            if User.objects.filter(username=username).exists():
                print("Username already exists")
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email already exists")
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
        else:
            print("Password not matching")
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')