from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Newsletter


def auth(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request, 'register.html')

    if 'signup' in request.POST:
        username = request.POST['email']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        roll_num = request.POST['rollno']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'message': 'Email already registered.'})

            # if User.objects.filter(email=email).exists():
            #     return render(request, 'register.html', {'message': 'Email already exist'})

            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=name)
            user.save()
            newsletter = Newsletter(user=user)
            # print(request.POST)
            newsletter.mobile = phone
            newsletter.roll_number = roll_num
            if 'isSubscribed' in request.POST:
                newsletter.isSubscribed = True
            newsletter.save()
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'message': 'Passwords do not match.'})
    else:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'message': 'Invalid credentials.'})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')
