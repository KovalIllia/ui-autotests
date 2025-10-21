import random
import secrets
import string
from faker import Faker
import random


def generate_password(lenght: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(lenght))


def generate_mobile_number():
    operator_codes = ["67", "68", "73", "93", "95", "96", "97", "98", "99"]
    operator = random.choice(operator_codes)
    return f"+380{operator}{random.randint(1000000, 9999999)}"
