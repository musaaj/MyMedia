from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    
    def _create_user(self, phone_number, password, is_staff, is_superuser, **extras):
        if not phone_number:
            raise ValueError('user must have a valid phone number')
        now = timezone.now()
        user = self.model(
                    phone_number=phone_number,
                    is_staff=is_staff,
                    is_superuser=is_superuser,
                    last_login=now,
                    date_joined=now,
                    **extras
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def creat_user(self, phone_number, password, **extras):
        return self._create_user(phone_number, password, False, False, **extras)

    def create_superuser(self, phone_number, password, **extras):
        return self._create_user(phone_number, password, True, True, **extras)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=256)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_absolute_url(self):
        return "users/%i/"%(self.pk)


class Todo(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User)
