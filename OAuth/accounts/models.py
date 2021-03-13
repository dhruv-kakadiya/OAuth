from django.db import models


# class UserToken(models.Model):
#     email = models.CharField(max_length=50, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     refresh_token = models.CharField(max_length=150)
#     access_token = models.CharField(max_length=150)
#     expires_at = models.DateTimeField()
#     token_type = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user
