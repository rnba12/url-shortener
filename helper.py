import random
import string

def shorten():
    random_url = ""
    for a in range(0,4):
        random_url += str(random.choice(string.ascii_lowercase)) + str(random.choice(string.digits))
    print(random_url)
    return random_url
