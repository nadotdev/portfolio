from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    """
        For user registration form and checking validation
    """
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # print(request.POST)
            user = register_form.save()
            login(request, user)
            
            return redirect('/')

    else:
        register_form = RegisterForm()
    return render(request, 'users/register.html', {'register_form': register_form})