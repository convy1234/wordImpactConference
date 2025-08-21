# registrations/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .form import RegistrationForm
from .models import Registration


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration received. See you at Word Impact ’25!")
            return redirect("registration_success")  # go to success page
    else:
        form = RegistrationForm()
    return render(request, "registrations/register.html", {"form": form})


def registration_success(request):
    return render(request, "registrations/registration_success.html")


def dashboard_login(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password == "#admin1234":  # set a strong password
            request.session["is_admin"] = True
            return redirect("dashboard")
    return render(request, "dashboard_login.html")


def dashboard(request):
    if not request.session.get("is_admin"):
        return redirect("dashboard_login")

    # --- filters & search ---
    search_query = request.GET.get("search", "")
    gender_filter = request.GET.get("gender", "")
    attendance_filter = request.GET.get("attendance", "")

    people = Registration.objects.all()

    # search by name or email
    if search_query:
        people = people.filter(
            first_name__icontains=search_query
        ) | people.filter(
            last_name__icontains=search_query
        ) | people.filter(
            email__icontains=search_query
        )

    # filter by gender
    if gender_filter:
        people = people.filter(gender=gender_filter)

    # filter by attendance
    if attendance_filter:
        people = people.filter(attendance=attendance_filter)

    # --- counts ---
    total_registered = Registration.objects.count()
    male_count = Registration.objects.filter(gender="Male").count()
    female_count = Registration.objects.filter(gender="Female").count()

    # --- pagination ---
    paginator = Paginator(people, 10)  # 10 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "total_registered": total_registered,
        "male_count": male_count,
        "female_count": female_count,
        "page_obj": page_obj,
        "search_query": search_query,
        "gender_filter": gender_filter,
        "attendance_filter": attendance_filter,
    }
    return render(request, "dashboard.html", context)
