import string
from random import choices, shuffle

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation


def generate_password(length: int = 8):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATIONS}"
    shuffle(list(printable))

    password = choices(printable, k=length)
    password = "".join(password)

    return password
