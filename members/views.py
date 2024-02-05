from django.contrib import messages
from django.shortcuts import render, redirect
from members.forms import UserLoginFrom, UserRegisterForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form_login = UserLoginFrom(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('main:starting_page')
    else:
        form_login = UserLoginFrom()
    return render(request, 'members/login_page.html', {'form_login': form_login})


def user_logout(request):
    logout(request)
    return redirect('main:starting_page')


def signup(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            join = User.objects.create_user(username=data['user_name'],
                                            email=data['email'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'],
                                            password=data['password1'])
            login(request, join)
            return redirect('main:starting_page')
    else:
        form_register = UserRegisterForm()
    return render(request, 'members/signup_page.html', {'signup': form_register})


@login_required()
def change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            new_pass1 = form.cleaned_data['new_pass1']
            request.user.set_password(new_pass1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect('main:starting_page')
        elif 'Your password was successfully updated.' in str(form.errors):
            form.errors.clear()
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'members/change_pass.html', {'form': form})
