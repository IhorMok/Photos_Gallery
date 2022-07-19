from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.first_name
