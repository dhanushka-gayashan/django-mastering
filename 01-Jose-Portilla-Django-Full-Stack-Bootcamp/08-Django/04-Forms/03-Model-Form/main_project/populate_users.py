# Set ENV Project
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_project.settings')

# Setup Django
import django
django.setup()


# Imports need to be done after Setup ENV and Django
import random
from faker import Faker
from users.models import User


# Create Faker Object
fakegen = Faker()


# Generate data for Users
def populate(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


# Execute Script to populate DB with Dummy Data
if __name__ == '__main__':
    print('starting data population......')
    populate(20)
    print('data population is completed...')