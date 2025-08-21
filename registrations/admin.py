from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "attendance",
        "church",
        "city",
        "created_at",
    )
    list_filter = ("gender", "attendance", "city", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "church", "city")
    ordering = ("-created_at",)
    list_per_page = 20  # paginate results for better viewing

    # Optional: make fields editable directly in list view
    list_editable = ("phone", "gender", "attendance", "city")

    # Optional: group fields in the detail view
    fieldsets = (
        ("Personal Info", {
            "fields": ("title", "first_name", "last_name", "gender", "email", "phone")
        }),
        ("Event Details", {
            "fields": ("attendance", "church", "city", "expectation")
        }),
        ("Consent", {
            "fields": ("consent",)
        }),
        ("Meta Info", {
            "fields": ("created_at",),
        }),
    )
    readonly_fields = ("created_at",)
