import random


def user():
    # make random username
    last_name = ["John", "Park", "Lee", "Kim"]
    first_name = ["james", "karthik", "murphy", "samuel"]
    username = []
    for i in range(100):
        username.append(random.choice(last_name) + " " + random.choice(first_name))
        password = random.randint(1000, 9999)

    print(password)


user()
