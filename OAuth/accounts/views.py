# from django.http.response import HttpResponse
# from django.shortcuts import render
from django.middleware import csrf
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from rest_framework.views import APIView

# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .credentials import CLIENT_ID, REDIRECT_URI, CLIENT_SECRET
from requests import post


class Home(APIView):
    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        print()
        print()
        print()
        print()
        print()
        print("Authenticated: ", authenticated)
        print()
        print()
        print()
        print()
        print("User: ", request.user)
        print()
        print()
        print()
        print()
        print()
        return Response({"message": "Home"}, status=status.HTTP_200_OK)


class AuthURL(APIView):
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        SCOPE = "profile+email"
        uri = (
            "https://accounts.google.com/o/oauth2/v2/auth?response_type=code"
            "&client_id={}&redirect_uri={}&scope={}"
        ).format(CLIENT_ID, REDIRECT_URI, SCOPE)
        return Response({"uri": uri}, status=status.HTTP_200_OK)


class LoginView(APIView):
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        code = request.GET["code"]
        data = {
            "code": code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        token = post("https://oauth2.googleapis.com/token", data=data)
        response = post("https://oauth2.googleapis.com/tokeninfo", data=token)
        data = response.json()

        user = User.objects.filter(email=data["email"]).first()
        if user is None:
            user = User.objects.create_user(email=data["email"], username=data["name"])
        login(request, user)
        print("Request User: ", request.user)
        return redirect("http://localhost:3000/")


class LogoutView(APIView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
        )


class CsrfTokenView(APIView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = csrf.get_token(request)
        return Response({"csrftoken": token}, status=status.HTTP_200_OK)