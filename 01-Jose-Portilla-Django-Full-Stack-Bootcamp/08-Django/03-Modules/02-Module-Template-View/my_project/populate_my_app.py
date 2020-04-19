# Set ENV Project
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Setup Django
import django
django.setup()


# Imports need to be done after Setup ENV and Django
import random
from faker import Faker
from my_app.models import AccessRecord, Topic, Webpage


# Create Faker Object
fakegen = Faker()


# Generate data for Topic
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t


# Generate data for Webpage and Access Record
def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


# Execute Script to populate DB with Dummy Data
if __name__ == '__main__':
    print('starting data population......')
    populate(20)
    print('data population is completed...')

