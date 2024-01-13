from django.shortcuts import render
from .forms import UserSignupForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def user_signup(request):
    if request.method == "POST":
        user_signup_form = UserSignupForm(data=request.POST)
        if user_signup_form.is_valid():
            user_signup_form.save()
            messages.success(request, "Account created successfully.")
        return render(request, "signup.html", {"user_signup_form": user_signup_form})
    user_signup_form = UserSignupForm()
    return render(request, "signup.html", {"user_signup_form": user_signup_form})


@login_required
def user_update_profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(instance=request.user, data=request.POST)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "Profile updated successfully.")
            return render(
                request, "update-profile.html", {"user_update_form": user_update_form}
            )
    user_update_form = UserUpdateForm(instance=request.user)
    return render(
        request, "update-profile.html", {"user_update_form": user_update_form}
    )


@login_required
def user_profile(request):
    return render(request, "profile.html")
