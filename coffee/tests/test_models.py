from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from coffee.models import Cafe


User = get_user_model()


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """setUpTestData: Run once to set up non-modified data for all class methods."""
        cls.test_user_1 = User.objects.create(username='test_user_1')
        cls.Client = Client()

    def setUp(self):
        """setUp: Run once for every test method to set up clean data."""
        pass

    def test_slug_label(self):
        """Method: test_false_is_false."""
        field_label = self.test_user_1._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')


class CafeTest(TestCase):
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
            rating=3.4
        )

    def setUp(self):
        """setUp: Run once for every test method to set up clean data."""
        self.cafe = Cafe.objects.get(name="Ziggy's")

    def test_name_label(self):
        field_label = self.cafe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.cafe._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)

    def test_description_label(self):
        field_label = self.cafe._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_rating_label(self):
        field_label = self.cafe._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    def test_rating_not_mandatory(self):
        """Rating field is not mandatory and for a newly created record defaults to None"""
        Cafe.objects.create(
            contributor=self.test_user_1,
            name="Cafe",
            description="Cafe with no rating",
            location="Sydenham",
        )
        cafe = Cafe.objects.get(name="Cafe")
        self.assertIsNone(cafe.rating)

    def test_rating_rounds_to_two_decimal_places(self):
        Cafe.objects.create(
            contributor=self.test_user_1,
            name="Cafe with ratings",
            description="Cafe created with over 2 decimal places",
            location="Sydenham",
            rating="4.39999"
        )
        cafe = Cafe.objects.get(name="Cafe with ratings")
        self.assertEqual(cafe.rating, Decimal('4.40'))

    def test_location_label(self):
        field_label = self.cafe._meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location')

    def test_get_absolute_url(self):
        self.assertEqual(self.cafe.get_absolute_url(), '/cafe/2')

    def test_dunder_str(self):
        """method: __str__"""
        str_representation = str(self.cafe)
        self.assertEqual(str_representation, "Ziggy's Sydenham test_user_1")

    def test_serialize(self):
        """Serialize to json"""
        cafe_serialized = self.cafe.serialize()
        self.assertDictEqual(cafe_serialized, {
            'cafe_id': 2,
            'name': "Ziggy's",
            'contributor': 'test_user_1',
            'description': 'Alas no longer',
            'rating': '3.40'
        })
