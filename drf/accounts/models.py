from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser ,PermissionsMixin, AbstractUser

# class UseProfFileMangerA(BaseUserManager):
#
#     def create_user(self, email, name, password=None):
#
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
# class User(AbstractUser):
#     email = models.EmailField(verbose_name='email', max_length=255, unique=True)
#     phone = models.CharField(null=True, max_length=255)
#     REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
#
#     USERNAME_FIELD = 'email'
#
#     def get_username(self):
#         return self.email


class UserProfileManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(name=name,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,email,password):
        user = self.create_user(name,email,password)
        user.is_superuser =True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length =200)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    objects = UserProfileManager()
    REQUIRED_FIELDS = ['name']
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email

class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CharField)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return  self.status_text
