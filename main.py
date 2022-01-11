import random, string; amt = input('How many passwords do you want to generate?: ')
for x in range(int(amt)):
    x = ('').join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(25, 125))); print(x); print(f'Password length is {len(x)}'); del x; del amt
