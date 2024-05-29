from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Course, Lesson


def home_page(request):
    return render(request, "./course/home.html")


def courses_page(request):
    courses = Course.objects.all()
    context = {"courses": courses}

    return render(request, "./course/courses.html", context)


def lessons_page(request, slug=None):
    course = get_object_or_404(Course, slug=slug)
    lessons = Lesson.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        lessons = Lesson.objects.filter(course=course)

    context = {"course": course, "lessons": lessons}
    return render(request, "./course/lessons.html", context)


def lesson_detail_page(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    lesson = get_object_or_404(Lesson, pk=pk)

    context = {"course": course, "lesson": lesson}

    return render(request, "./course/lesson-detail.html", context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login_page")
    else:
        form = NewUserForm()

    context = {"form": form}
    return render(request, "./user/sign-up.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("courses_page")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "./user/login.html", context)


def logut_request(request):
    logout(request)
    return redirect("home_page")
