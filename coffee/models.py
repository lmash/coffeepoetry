from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class User(AbstractUser):
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)


class CoffeeShop(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    name = models.TextField(max_length=250)
    description = models.TextField()
    image_1 = models.TextField(max_length=250, null=True)
    image_2 = models.TextField(max_length=250, null=True)
    image_3 = models.TextField(max_length=250, null=True)
    rating = models.DecimalField(null=True, decimal_places=2, max_digits=3)

    def __str__(self):
        return f"{self.name} {self.creator}"

    def get_absolute_url(self):
        pass

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "creator": self.creator,
            "description": self.description,
            "image_1": self.image_1,
            "image_2": self.image_2,
            "image_3": self.image_3,
            "rating": self.rating
        }


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE_BEAN = 1
        TWO_BEANS = 2
        THREE_BEANS = 3
        FOUR_BEANS = 4
        FIVE_BEANS = 5

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quality = models.IntegerField(choices=Rating.choices)
    latte_art = models.IntegerField(choices=Rating.choices)
    barrista_friendliness = models.IntegerField(choices=Rating.choices)
    price = models.IntegerField(choices=Rating.choices)
    opening_hours = models.IntegerField(choices=Rating.choices)
    score = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return f"{self.reviewer} {self.coffee_shop} {self.created_at}"

    def serialize(self):
        return {
            "id": self.id,
            "reviewer": self.reviewer,
            "coffee_shop": self.coffee_shop,
            "created_at": self.created_at,
            "quality": self.quality,
            "latte_art": self.latte_art,
            "barrista_friendliness": self.barrista_friendliness,
            "price": self.price,
            "opening_hours": self.opening_hours
        }


class Adjective(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    adjective = models.TextField(max_length=50)


class Poem(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    haiku = models.TextField()
