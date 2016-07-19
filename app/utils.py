# Any utility functions would go here
import string, random

def hash_generator(size=8,
                   chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
