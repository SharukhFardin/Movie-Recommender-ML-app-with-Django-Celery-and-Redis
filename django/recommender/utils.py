import csv

from django.conf import settings

from faker import Faker

# DATA_DIR = seetiin


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
