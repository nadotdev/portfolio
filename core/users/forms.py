from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class RegisterForm(UserCreationForm):
    """
        Custom user registration form
    """
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm mb-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm mb-2'

        """
            Disabled help_text to user when render to template
        """
        self.fields['password1'].help_text = {}
        self.fields['password2'].help_text = {} 

        self.fields['password1'].error_messages = {}
        self.fields['password2'].error_messages = {} 

    email = forms.EmailField(max_length=200)
    captcha = ReCaptchaField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'captcha')

    email.widget.attrs.update({"class": "form-control form-control-sm mb-2"})
