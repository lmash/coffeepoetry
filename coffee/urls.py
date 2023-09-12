from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("my_cafes", views.MyCafesView.as_view(), name="my_cafes"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("new", views.new_cafe, name="new"),
    path("cafe/<int:cafe_id>", views.cafe_view, name="cafe"),
    path("review/<int:cafe_id>", views.review_view, name="review"),
    path("rating/<int:cafe_id>", views.rating_view, name="rating"),
    path("haiku/<int:cafe_id>", views.haiku_view, name="haiku"),
    path("save_edit/<int:cafe_id>", views.save_edited_view, name="save_edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
