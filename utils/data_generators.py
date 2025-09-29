import secrets
import string


def generate_password(lenght:int=10)->str:
    alphabet=string.ascii_letters+string.digits+string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(lenght))
