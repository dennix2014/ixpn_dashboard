import random
import string

ALPHANUMERIC_STRING = string.ascii_lowercase + string.digits
STRING_LENGTH = 4

def generate_random_string(chars=ALPHANUMERIC_STRING, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


