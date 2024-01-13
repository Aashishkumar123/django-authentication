from django.urls import path
from .views import user_signup, user_update_profile, home, user_profile
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)


urlpatterns = [
    path("", home, name="home"),
    path("signup/", user_signup, name="user-signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="user-login"),
    path("profile/update/", user_update_profile, name="user-update-profile"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
    path(
        "profile/update/password/",
        PasswordChangeView.as_view(template_name="update-password.html"),
        name="user-update-password",
    ),
    path(
        "profile/update/password/done/",
        PasswordChangeDoneView.as_view(template_name="update-password-done.html"),
        name="password_change_done",
    ),
    path("profile/", user_profile, name="user-profile"),
]
