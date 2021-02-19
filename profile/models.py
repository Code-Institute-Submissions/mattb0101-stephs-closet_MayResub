from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    """
    User Account that the customer will be
    able to see their order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
