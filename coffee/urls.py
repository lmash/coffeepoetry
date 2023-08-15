from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("new", views.new_cafe, name="new"),
    path("cafe/<int:cafe_id>", views.cafe_view, name="cafe"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

