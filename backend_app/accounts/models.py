from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User Account with the given email and password.
        """
        if not email:
            raise ValueError('Account must have an email address.')

        account = self.model(
            email=self.normalize_email(email)
        )
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_staffuser(self, email, password):
        """
        Creates and saves a Staff Account user with the given email and password.
        """
        account = self.create_user(
            email,
            password=password,
        )
        account.is_staff = True
        account.save(using=self._db)
        return account

    def create_superuser(self, email, password):
        """
        Creates and saves a Superuser Account with the given email and password.
        """
        account = self.create_user(
            email,
            password=password,
        )
        account.is_staff = True
        account.is_superuser = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email_address',
        unique=True,
        max_length=255
    )
    # notice the absence of a 'Password field' , that's built in.
    created_on = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=128, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # A SUPER USER
    last_login = models.DateTimeField(null=True, blank=True)
    forgot_password_token = models.CharField(max_length=120, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # email and password are required by default

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def staff(self):
        """Is the user a member of staff?"""
        return self.is_staff

    @property
    def superuser(self):
        """Is the user a admin member?"""
        return self.is_superuser

    @property
    def active(self):
        """Is the user active?"""
        return self.is_active

    objects = AccountManager()
