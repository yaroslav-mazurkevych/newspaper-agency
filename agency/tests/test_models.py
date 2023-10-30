from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class TopicTests(TestCase):
    def test_car_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic), topic.name)


class RedactorTests(TestCase):
    def test_driver_str(self):
        redactor = get_user_model().objects.create(
            years_of_experience=10,
            username="test-name",
            password="test123456",
            first_name="test-first",
            last_name="test-last",
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username}: ({redactor.first_name} {redactor.last_name})"
        )


class NewspaperTests(TestCase):
    def test_manufacturer_str(self):
        newspaper = Newspaper.objects.create(
            title="test-title",
            content="test-content",
        )
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} Publishers: {newspaper.publishers}"
        )
