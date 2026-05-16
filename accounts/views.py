from django.contrib import auth, messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm
from accounts.models import VerifyCode
from accounts.utils import send_email


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
                messages.error(request, 'username yoki password xato')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def forgot_password(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        # Userni topamiz
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(request, 'User topilmadi')
            return redirect('accounts:forgot_password')

        # Code yaratamiz
        code_obj = VerifyCode.objects.create(user=user)

        # Email yuboramiz
        send_email(
            subject='Parolni tiklash',
            message=f"Sizning codingiz: {code_obj.code}\nCode 2 daqiqa ishlaydi.",
            recipient_email=user.email,
        )

        messages.success(request, 'Emailingizga code yuborildi')
        return redirect('accounts:restore_password')

    return render(request, 'account/forgot_password.html')


def restore_password(request):

    if request.method == 'POST':

        code = request.POST.get('code')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Parollar tekshiriladi
        if new_password != confirm_password:
            messages.error(request, 'Parollar mos emas')
            return redirect('accounts:restore_password')

        # Codeni topamiz
        try:
            code_obj = VerifyCode.objects.get(code=code)

        except VerifyCode.DoesNotExist:
            messages.error(request, 'Code invalid')
            return redirect('accounts:restore_password')

        # Code eskirmaganmi
        if not code_obj.is_valid():
            messages.error(request, 'Code eskirgan')
            return redirect('accounts:restore_password')

        # Password yangilanadi
        user = code_obj.user
        user.set_password(new_password)
        user.save()

        # Codeni o‘chiramiz
        code_obj.delete()

        messages.success(request, 'Parol muvaffaqiyatli yangilandi')
        return redirect('accounts:login')

    return render(request, 'account/restore_password.html')