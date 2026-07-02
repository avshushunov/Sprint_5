import random

def generate_email():
    return f"user{random.randint(1000, 9999)}@test.com"

def generate_name_ad():
    return f"Продам товар № {random.randint(1, 9999)}"

def value_password():
    return "Password123"