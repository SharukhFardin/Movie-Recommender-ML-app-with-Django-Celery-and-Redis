from faker import Faker


def get_fake_profiles(count=10):
    # Generates fake profile data
    fake = Faker()
    user_data = []

    for _ in range(10):
        profile = fake.profile()
        data = {
            "username": profile.get("username"),
            "email": profile.get("mail"),
            "is_active": True,
        }
        if "name" in profile:
            fname, lname = profile.get("name").split(" ")[:2]
        user_data.append(data)
    return user_data