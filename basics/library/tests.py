from django.test import TestCase
from .models import LB_User
# Create your tests here.

class ModelTesting(TestCase):


    def test_user_model(self):
        test_user = LB_User.objects.create(username='Abhishek', email='abhi@g.com')
        get_user = LB_User.objects.get(id=test_user.id)

        self.assertTrue(isinstance(test_user, LB_User))

        self.assertEqual(get_user.username, 'Abhishek')
        self.assertEqual(get_user.email, 'abhi@g.com')
        self.assertEqual(str(get_user), 'Abhishek')