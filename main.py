import random, string; amt = input('How many passwords do you want to generate?: ')
for x in range(int(amt)):
    # generate a random string using ascii, digits, and punctuation, varying 25-125 in length
    x = ('').join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(25, 125)))
    # we reverse the string as to not be predictable with the random module
    print(x[::-1]) 
    print(f'Password length is {len(x)}')
    # delete variable from memory
    del x
