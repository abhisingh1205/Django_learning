from django.core.management.base import BaseCommand
from faker import Faker
from .views import Student
import random

class FakeCommand(BaseCommand):
    help = 'Generate fake students in models'

    def help(self, *args, **kwargs):
        fake = Faker()

        num_records = 20

        for _ in range(num_records):

            Student.objects.create(
                name = fake.name(),
                roll_no = random.randint(30, 100),
                city = fake.address(),
                marks = random.randint(80, 100),
                pass_date = fake.date_time_this_year()
            )
            