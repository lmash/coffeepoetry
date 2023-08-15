from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import OuterRef, Subquery
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Cafe, User, Image
from .forms import CafeForm


class HomeView(ListView):
    model = Cafe
    template_name = "coffee/index.html"

    def get_queryset(self):
        cafes = (
            Cafe.objects
            .all()                                  # Get all Cafe's
            .order_by('-rating', 'name')            # Order by descending rating and then name
            .annotate(first_photo=Subquery(         # Add the first image found for the Cafe
                Image.objects.filter(
                    cafe_id=OuterRef('pk'))
                .values('name')[:1]))
        )

        return cafes


@method_decorator(login_required, name='dispatch')
class MyCafesView(ListView):
    model = Cafe
    template_name = "coffee/my_cafes.html"

    def get_queryset(self):
        cafes = (
            Cafe.objects                            # Get Cafe's
            .filter(contributor=self.request.user)  # Filter by logged in user
            .order_by('-rating', 'name')            # Order by descending rating and then name
            .annotate(first_photo=Subquery(         # Add the first image found for the Cafe
                Image.objects.filter(
                    cafe_id=OuterRef('pk'))
                .values('name')[:1]))
        )

        return cafes


def cafe_view(request):
    return render(request, "coffee/cafe.html")


@login_required(login_url='login')
def new_cafe(request):
    if request.method == "POST":

        # Populate cafe with the user who is logged in
        cafe = Cafe(contributor=request.user)
        cafe_form = CafeForm(request.POST, instance=cafe)
        images = request.FILES.getlist('images')

        if cafe_form.is_valid():
            cafe_form.save()

            for image in images:
                Image.objects.create(
                    cafe=cafe,
                    name=image
                )

            return redirect('index')
    else:
        cafe_form = CafeForm()

    return render(request=request, template_name="coffee/new.html", context={'cafe_form': cafe_form})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "coffee/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "coffee/login.html")


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "coffee/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "coffee/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect('index')
    else:
        return render(request, "coffee/register.html")
