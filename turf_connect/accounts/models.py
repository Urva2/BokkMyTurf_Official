from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with email-based login and role-based access."""

    class Role(models.TextChoices):
        PLAYER = 'player', 'Player'
        OWNER = 'owner', 'Owner'
        ADMIN = 'admin', 'Admin'

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.PLAYER,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
