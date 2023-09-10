from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    # TODO At the end look to see whether slug field is ever used, if not remove
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)


class Cafe(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributor')
    name = models.TextField(max_length=250)
    description = models.TextField()
    rating = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    location = models.TextField(max_length=250)
    check_for_haiku = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.location} {self.contributor}"

    def get_absolute_url(self):
        return reverse('cafe', kwargs={'cafe_id': self.id})

    def serialize(self):
        return {
            "cafe_id": self.id,
            "name": self.name,
            "contributor": self.contributor.username,
            "description": self.description,
            "rating": str(self.rating)
        }


class Image(models.Model):
    cafe = models.ForeignKey(Cafe, default=None, on_delete=models.CASCADE)
    name = models.ImageField(upload_to='images/', verbose_name='Image')

    def __str__(self):
        return f"{self.cafe} {self.name}"

    def serialize(self):
        return {
            "cafe_id": self.cafe,
            "name": self.name
        }


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quality = models.IntegerField(choices=Rating.choices)
    latte_art = models.IntegerField(choices=Rating.choices)
    barrista_friendliness = models.IntegerField(choices=Rating.choices)
    price = models.IntegerField(choices=Rating.choices)
    opening_hours = models.IntegerField(choices=Rating.choices)
    score = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return f"{self.reviewer} {self.cafe} {self.created_at}"

    def serialize(self):
        return {
            "id": self.id,
            "reviewer": self.reviewer,
            "cafe": self.cafe,
            "created_at": self.created_at,
            "quality": self.quality,
            "latte_art": self.latte_art,
            "barrista_friendliness": self.barrista_friendliness,
            "price": self.price,
            "opening_hours": self.opening_hours
        }


class CoffeeDescription(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=250)


class Poem(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    haiku = models.TextField()
    inspiration_1 = models.ForeignKey(CoffeeDescription, on_delete=models.CASCADE, related_name='inspiration_1')
    inspiration_2 = models.ForeignKey(CoffeeDescription, on_delete=models.CASCADE, related_name='inspiration_2')
    inspiration_3 = models.ForeignKey(CoffeeDescription, on_delete=models.CASCADE, related_name='inspiration_3')
