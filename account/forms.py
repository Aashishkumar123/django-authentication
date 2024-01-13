from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    ...


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
