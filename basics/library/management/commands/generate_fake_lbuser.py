from django.core.management.base import BaseCommand
from faker import Faker
from ...models import LB_User
import random

class Command(BaseCommand):
    help = 'Generate fake lb_users in models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_records = 20

        for _ in range(num_records):

            LB_User.objects.create(
                username = fake.name(),
                email = fake.email()
            )

