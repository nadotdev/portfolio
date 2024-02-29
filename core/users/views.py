from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def register(request):
    """
        For user registration form and checking validation
    """
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        # recaptcha_form = FormWithCaptcha(request.POST)
        if register_form.is_valid():
            user = register_form.save() # Save to database
            user.is_active = False # Set status to inactive
            user.save() # Save again
            return redirect('/in-review')

    else:
        register_form = RegisterForm()
        # recaptcha_form = FormWithCaptcha()

    context = {
        'register_form': register_form,
        # 'recaptcha_form': recaptcha_form
    }
    return render(request, 'users/register.html', context)
