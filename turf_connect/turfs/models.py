from django.conf import settings
from django.db import models


class Turf(models.Model):
    """Represents a turf listing submitted by an owner."""

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='turfs',
    )
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.city} ({self.get_status_display()})"


class Slot(models.Model):
    """Represents a bookable time slot for a turf."""

    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        BOOKED = 'booked', 'Booked'

    turf = models.ForeignKey(
        Turf,
        on_delete=models.CASCADE,
        related_name='slots',
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )

    def __str__(self):
        return f"{self.turf.name} | {self.date} {self.start_time}–{self.end_time} ({self.get_status_display()})"
