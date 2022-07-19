from django.contrib.auth.backends import BaseBackend
from photos_gallery.gallery.models import User
from django.contrib.auth.hashers import check_password


# 1 Find user by email
# 2 Use "check_password" method to compare password to request and password field of the model
# 3 return model User if check_password method will return "True", otherwise "None"
# 4 Register in setting DJANGO apps


class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return None
        # if user is not None and user.check_password(password):
        #     if user.is_active == Constants.YES:
        #         return user
        # return None
        user = User.objects.get(email=email)
        if user is not None and user.check_password(password):
            if user.is_active:
                return user
            else:
                return "User is not activated"
        else:
            return None
