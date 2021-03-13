from .models import UserToken
from django.utils import timezone
from datetime import timedelta

# from .credentials import CLIENT_ID, CLIENT_SECRET
# from requests import post, put, get


def get_user_token(usermail):
    userToken = UserToken.objects.filter(email=usermail).first()
    return userToken
    # if userToken.exists():
    #     return userToken
    # else:
    #     return None


def create_or_update_user(
    userEmail, access_token, token_type, refresh_token, expires_in
):
    tokens = get_user_token(userEmail)
    expires_at = timezone.now() + timedelta(seconds=expires_in)

    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_at = expires_at
        tokens.token_type = token_type
        tokens.save(
            update_fields=["access_token", "refresh_token", "expires_at", "token_type"]
        )
    else:
        tokens = UserToken(
            email=userEmail,
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_at=expires_at,
        )
        tokens.save()
