import string
import secrets


def generate_secret_key(n: int) -> str:
    sec = string.ascii_letters + string.digits + string.ascii_uppercase + string.punctuation
    key = ''.join(secrets.choice(sec) for _ in range(n))
    return key
