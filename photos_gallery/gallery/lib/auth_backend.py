import logging
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from gallery.models import User


class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        user = User.objects.get(email=email)
        logging.info(user)
        if user is not None and check_password(password, user.password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            user = User._default_manager.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user