from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import CreateUserForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'Username of password is incorrect')
    return render(request, 'user/login.html')

def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form=CreateUserForm()
    return render(request, 'user/registration.html', {'register_form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
