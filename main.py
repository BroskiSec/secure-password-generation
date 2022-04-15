import string
import argparse
import secrets
import random

parser = argparse.ArgumentParser()
parser.add_argument('amount', help='amount of passwords to generate', type=int)
args = parser.parse_args()

for x in range(int(args.amount)):
    x = string.ascii_letters + string.digits + string.punctuation 
    x = ''.join(secrets.choice(x) for i in range(random.randint(50, 250)))
    print(x[::-1]) 
    print(f'Password length is {len(x)}')
    del x
