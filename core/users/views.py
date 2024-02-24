from django.shortcuts import render, redirect
# from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    """
        For user registration form and checking validation
    """
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save() # Save to database
            user.is_active = False # Set status to inactive
            user.save() # Save again
            # user = register_form.save()
            # if user
            # login(request, user)
            return redirect('/in-review')

    else:
        register_form = RegisterForm()
    return render(request, 'users/register.html', {'register_form': register_form})