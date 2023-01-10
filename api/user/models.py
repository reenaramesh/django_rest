from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    '''
class CustomUser(AbstractUser):
    name = models.CharField(max_length=250, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)

# sign up user using email and name
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    phone = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)

    session_token = models.CharField(max_length=35, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # objects = CustomUserManager()

    def __str__(self):
        return self.emai'''


from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email