from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True,null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email

    def email_user(self, subject, message):
        send_mail(
        subject,
        message,
        'anthonymensah1030@gmail.com',
        [self.email],
        fail_silently=False,
        )
