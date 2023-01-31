import random

def shorten():
    random_url = ""
    list2 = ["z", "y", 1, 2, 3, 4, 5, 6, 7, 8, 9, "c", "a", "q", "w"]
    for a in range(0,7):
        random_url += str(random.choice(list2))
    print(random_url)
    return random_url