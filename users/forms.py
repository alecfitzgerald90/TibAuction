from django import forms
from users.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
import secrets
import string
from phonenumber_field.formfields import PhoneNumberField




class CreateUserForm(UserCreationForm):
    """
    A UserCreationForm with optional password inputs.
    """

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "groups")

    def save(self, commit=True):
        password = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(8)))
        user = super(CreateUserForm, self).save()
        user.set_password(password)
        user.groups.set(self.cleaned_data["groups"])
        user.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'


