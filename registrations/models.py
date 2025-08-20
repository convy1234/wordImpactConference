from django.db import models

# Create your models here.
from django.db import models


class Registration(models.Model):
    class AttendanceType(models.TextChoices):
        IN_PERSON = "in-person", "In-Person"
        ONLINE = "online", "Online"

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)  # Prevents duplicate emails
    phone = models.CharField(max_length=20, blank=True)

    attendance = models.CharField(
        max_length=12,
        choices=AttendanceType.choices,
        default=AttendanceType.IN_PERSON,
    )

    church = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=80, blank=True)

    expectation = models.TextField(
        blank=True,
        null=True,
        help_text="What do you hope to gain from this event?"
    )

    consent = models.BooleanField(default=False)  # e.g. for data/privacy consent
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_attendance_display()})"
