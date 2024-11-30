import string
from random import sample


def generate_password():
    return ''.join(
        sample(string.ascii_letters + string.digits + string.punctuation, 12)
    )
