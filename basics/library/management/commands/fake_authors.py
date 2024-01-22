from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Author, LB_User
import random

class Command(BaseCommand):
    help = 'Generate fake lb_users in models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_records = 20

        lb_users = LB_User.objects.values_list('id', flat=True)

        for ele in lb_users:
            print("Id = ", ele)

        print("random choice = {}".format(random.choice(lb_users)))
        for _ in range(num_records):

            auth_obj = Author(
                firstname = fake.first_name(),
                lastname = fake.last_name(),
                joindate = fake.date_this_decade(),
                popularity_score = random.randint(1, 10)
            )

            auth_obj.save()
            auth_obj.followers.add(LB_User.objects.get(id=random.choice(lb_users)))

