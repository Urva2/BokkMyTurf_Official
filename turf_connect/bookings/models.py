from django.conf import settings
from django.db import models


class Booking(models.Model):
    """Represents a player's booking of a turf slot."""

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    slot = models.ForeignKey(
        'turfs.Slot',
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return f"Booking #{self.pk} — {self.player.username} | {self.slot} ({self.get_status_display()})"
