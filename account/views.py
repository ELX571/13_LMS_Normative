from django.contrib import auth
from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('u13_project:book_list')

    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                auth_login(request, user)
                return redirect('u13_project:book_list')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')