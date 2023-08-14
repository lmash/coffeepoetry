from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("new", views.new_cafe, name="new"),
    path("cafe/<int:cafe_id>", views.cafe_view, name="cafe"),
]