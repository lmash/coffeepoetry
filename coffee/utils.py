import dataclasses
from django.db.models import Sum
import random

from coffee.ai import get_haiku
from .models import Cafe, CoffeeDescription, Review, Poem


sayings = [
    'The AI is uninspired',
    'Excellence begets creativity',
    'Perhaps being more detailed would help',
    "I won't get out of bed for anything less than 4 stars",
    'A wise man said...',
    'The AI is not inspired',
    'zzzzzzzzzzz',
]


@dataclasses.dataclass
class Haiku:
    line_1: str
    line_2: str
    line_3: str


def update_cafe_rating(cafe):
    """Calculate the cafe rating as the average of scores"""
    total = (Review.objects.all().filter(cafe=cafe).aggregate(Sum('score')))
    num_reviews = (Review.objects.all().filter(cafe=cafe).count())
    cafe.rating = total['score__sum']/num_reviews
    cafe.save()


def update_coffee_description(cafe, data):
    """Update the coffee description with the text entered"""
    description = CoffeeDescription(
        cafe=cafe,
        description=data['coffee_description']
    )
    description.full_clean()
    description.save()


def add_cafe_for_poetry_generation(cafe):
    """Mark the cafe as eligible for poetry generation"""
    cafe = Cafe.objects.get(id=cafe.pk)
    cafe.check_for_haiku = True
    cafe.save()


def cafe_eligible(cafe) -> bool:
    """A café is only eligible if it has 3 or more CoffeeDescription rows and a rating of 4 or more"""
    return CoffeeDescription.objects.filter(cafe=cafe.pk).count() >= 3 and cafe.rating >= 4


def get_random_coffee_descriptions(cafe) -> str:
    """Returns a '.' delimited string with 3 random descriptions"""
    coffee_descriptions_query_set = (
        CoffeeDescription.objects
        .filter(cafe=cafe.pk)
        .order_by('pk')
        .values("description")
    )

    descriptions = [
        description
        for value in coffee_descriptions_query_set
        for description in value.values()
    ]

    return ". ".join(random.sample(descriptions, 3))


def get_cafe_and_coffee_descriptions(cafe) -> (str, str):
    """
    Returns a tuple of 2 strings
     - the cafe description
     - the coffe descriptions (3 of them)
    """
    cafe_description = Cafe.objects.get(id=cafe.pk).description
    coffee_descriptions = get_random_coffee_descriptions(cafe)

    return cafe_description, coffee_descriptions


def joining_the_dots(cafe):
    """Iterate over poetry candidates, where eligible generate a haiku, save it and reset check_for_haiku to False"""
    Cafe.objects.filter(id=cafe.pk).update(check_for_haiku=False)

    if not cafe_eligible(cafe):
        return

    cafe_description, coffee_descriptions = get_cafe_and_coffee_descriptions(cafe)
    haiku = get_haiku(cafe=cafe_description, coffee=coffee_descriptions)

    poem = Poem(
        cafe=cafe,
        haiku=haiku,
        inspiration=coffee_descriptions
    )
    poem.save()


def get_haiku_lines(cafe) -> Haiku:
    """Returns the most recent haiku as 3 strings"""
    try:
        poem = Poem.objects.filter(cafe=cafe.id).latest('created_at')
        lines = poem.haiku.split("\n")
        return Haiku(line_1=lines[0], line_2=lines[1], line_3=lines[2])
    except Poem.DoesNotExist:
        return Haiku(line_1="", line_2="", line_3="")


def default_missing_inspiration(cafes):
    """"Get inspiration from list of sayings if missing"""
    for cafe in cafes:
        if cafe.haiku is None:
            cafe.haiku = ""
            cafe.inspiration = random.choice(sayings)

    return cafes
