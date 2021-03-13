from django.urls import path
from .views import AuthURL, LoginView, LogoutView, Home, CsrfTokenView

urlpatterns = [
    path("home/", Home.as_view()),
    path("csrf-token/", CsrfTokenView.as_view()),
    path("get-auth-url/", AuthURL.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
