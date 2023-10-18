import csv
import datetime

from pprint import pprint
from django.conf import settings

from faker import Faker

MOVIE_METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"


def load_movie_data(limit=10):
    with open(MOVIE_METADATA_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader)

def get_fake_profiles(count=10):
    # Generates fake profile data
    fake = Faker()
    user_data = []

    for _ in range(count):
        profile = fake.profile()
        data = {
            "username": profile.get("username"),
            "email": profile.get("mail"),
            "is_active": True,
        }
        if "name" in profile:
            fname, lname = profile.get("name").split(" ")[:2]
            data["first_name"] = fname
            data["last_name"] = lname
        user_data.append(data)
    return user_data
