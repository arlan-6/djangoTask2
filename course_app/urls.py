from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("courses/", views.courses_page, name="courses_page"),
    path("courses/<slug:slug>/", views.lessons_page, name="lessons_page"),
    path(
        "courses/<slug:slug>/<int:pk>/",
        views.lesson_detail_page,
        name="lesson_detail_page",
    ),
    path("user/sign-up", views.sign_up_page, name="sign_up_page"),
    path("user/login", views.login_page, name="login_page"),
    path("user/logout", views.logut_request, name="logut_request"),
]
