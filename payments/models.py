from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    PROVIDER_CHOICES = [
        ('click', 'Click'),
        ('payme', 'Payme'),
        ('stripe', 'Stripe'),
        ('manual', 'Manual'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES,
        default='manual'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.status})"