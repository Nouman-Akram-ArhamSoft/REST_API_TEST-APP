from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="TODO APP"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class Task(models.Model):
    task_title = models.CharField(max_length=200, blank=False)
    task_description = models.TextField(blank=True)
    is_complete = models.BooleanField(blank=False, default=False)

    # Category variables
    HT = 'Home Task'
    OT = 'Office Task'
    MISC = 'Miscellaneous Task'

    category = [
        (HT, "Home Task"),
        (OT, "Office Task"),
        (MISC, 'Miscellaneous')
    ]

    task_category = models.CharField(max_length=20, choices=category, blank=False)
    task_start_date = models.DateTimeField(default=datetime.now())
    task_end_date = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
