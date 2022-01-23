import random 
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('amount', help='amount of passwords to generate', type=int)
args = parser.parse_args()

for x in range(int(args.amount)):
    # generate a random string using ascii, digits, and punctuation, varying 25-250 characters in length
    x = ('').join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(25, 250)))
    # we reverse the string as to not be predictable with the random module
    print(x[::-1]) 
    print(f'Password length is {len(x)}')
    # delete variable from memory
    del x
