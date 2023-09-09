from django.db.models import Sum
from dotenv import load_dotenv
import os
import openai
import random


from .models import Cafe, CoffeeDescription, Review


# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def reduce_content(text: str) -> str:
    """Given content return a single haiku only (sometimes the API returns more than one haiku)"""
    lines = text.split('\n')
    return "\n".join((lines[0], lines[1], lines[2]))


def get_haiku(cafe: str = None, coffee: str = None) -> str:
    """
        AI call to generate a haiku based on cafe and coffee descriptions provided
        Returns haiku
    """
    if not coffee:
        coffee = """
                    perfectly roasted bean
                    pretty latte art 
                    tasty
                    dark
        """

    if not cafe:
        cafe = """This is the best coffee in the area by far. The people are always friendly."""

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"""
            You are a master haiku writer. 
            Write a haiku about a speciality coffee cafe which is described below. The haiku should be visual and dreamy 
            with occasional scenic or color references. Never mention prices. 
    
            Below: {coffee}

            The cafe is described as: {cafe}
            
            A single 3 line haiku should be returned
            """
                   }],
        temperature=0.7,
    )

    content = chat_completion.choices[0].message.content
    haiku = reduce_content(content)
    return haiku


def update_cafe_rating(cafe):
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
    """A café is only eligible if it has 3 or more CoffeeDescription rows"""
    return CoffeeDescription.objects.filter(cafe=cafe.pk).count() >= 3


def get_random_coffee_descriptions():
    pass


def get_cafe_and_coffee_descriptions(cafe) -> (str, str):
    """
    Get the records matching the cafe provided
    Select 3 cafe descriptions randomly
    Returns a tuple of 2 strings (cafe_descriptions, coffee_descriptions)
    """
    cafe_description = Cafe.objects.get(id=cafe.pk).description
    if cafe_eligible():
        coffee_descriptions = ""

    return "", ""

# poem = get_haiku()
# print(poem)
