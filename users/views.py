from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect("jobs")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("login")

@login_required
def jobs(request):
    job_list = [
        {"title": "Django Developer", "location": "Remote"},
        {"title": "Frontend Engineer", "location": "Bangalore"},
    ]
    return render(request, "users/jobs.html", {"jobs": job_list})
