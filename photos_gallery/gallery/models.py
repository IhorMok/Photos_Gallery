from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.first_name


class Album(models.Model):
    name = models.CharField(max_length=128)
    public = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Picture(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="picture/%Y/%m/%d/")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
