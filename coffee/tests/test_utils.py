from django.contrib.auth import get_user_model
from django.test import TestCase, Client


from coffee import utils
from coffee.models import Cafe, CoffeeDescription


User = get_user_model()


def test_content_of_haiku_reduced_to_first_three_lines():
    content = "Golden beans dancing,\nLatte art blooming with love,\nTaste of darkness, bliss.\n\n" \
              "Friendly souls unite,\nIn this haven of aroma,\nBest coffee, by far."
    assert utils.reduce_content(content) == "Golden beans dancing,\n" \
                                            "Latte art blooming with love,\n" \
                                            "Taste of darkness, bliss."


class UtilsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """setUpTestData: Run once to set up non-modified data for all class methods."""
        cls.test_user_1 = User.objects.create(username='test_user_1')
        cls.Client = Client()
        Cafe.objects.create(
            contributor=cls.test_user_1,
            name="Ziggy's",
            description="Alas no longer",
            location="Sydenham",
            rating=3.4,
            check_for_haiku=True
        )

    def setUp(self):
        """setUp: Run once for every test method to set up clean data."""
        self.cafe = Cafe.objects.get(name="Ziggy's")
        CoffeeDescription.objects.create(
            cafe=self.cafe,
            description='Smooth and mellow with hints of orange'
        )
        CoffeeDescription.objects.create(
            cafe=self.cafe,
            description='Bubbly and truly delicious.. invigorating'
        )
        CoffeeDescription.objects.create(
            cafe=self.cafe,
            description='Roasted'
        )

    def test_cafe_eligible_where_3_descriptions_exist(self):
        assert utils.cafe_eligible(self.cafe) is True

    def test_cafe_not_eligible_when_no_descriptions(self):
        cafe = Cafe.objects.create(
            contributor=self.test_user_1,
            name="Test Cafe",
            description="Test Cafe",
            location="",
        )
        assert utils.cafe_eligible(cafe) is False

    def test_random_coffee_descriptions(self):
        three_descriptions = utils.get_random_coffee_descriptions(self.cafe)
        assert three_descriptions.find('Smooth and mellow with hints of orange') != -1
        assert three_descriptions.find('Bubbly and truly delicious.. invigorating') != -1
        assert three_descriptions.find('Roasted') != -1
