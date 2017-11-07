from django import forms
from .models import MyUser


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = MyUser
        fields = ('username', 'avatar', 'email', )
