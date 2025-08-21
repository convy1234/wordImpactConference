from django.db import models

# Create your models here.
from django.db import models
class Registration(models.Model):
    class AttendanceType(models.TextChoices):
        IN_PERSON = "in-person", "In-Person"
        ONLINE = "online", "Online"

    class TitleChoices(models.TextChoices):
        MR = "Mr", "Mr"
        MRS = "Mrs", "Mrs"
        MISS = "Miss", "Miss"
        PASTOR = "Pastor", "Pastor"
        REV = "Rev", "Rev"

    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    title = models.CharField(max_length=10, choices=TitleChoices.choices, default=TitleChoices.MR)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    gender = models.CharField(max_length=10, choices=GenderChoices.choices, blank=True)

    attendance = models.CharField(
        max_length=12,
        choices=AttendanceType.choices,
        default=AttendanceType.IN_PERSON,
    )

    church = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=80, blank=True)
    expectation = models.TextField(blank=True, null=True)
    consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} ({self.get_attendance_display()})"
