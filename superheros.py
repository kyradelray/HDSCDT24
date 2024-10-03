names= ['Sian', 'Kat','Estelle','Kyra','Austin','Josh','Dylan','Anda','Anna','Sarah']


import random

def generate_superhero_name(inputname):
    adjectives = ["Mighty", "Invisible", "Speedy", "Clever", "Fearless", "Fierce"]
    animals = ["Falcon", "Dragon", "Tiger", "Shark", "Panther", "Wolf"]
    colors = ["Red", "Blue", "Green", "Golden", "Silver", "Black"]

    name = f"{random.choice(adjectives)} {random.choice(colors)} {random.choice(animals)} "+ inputname 

    return name


print("\nSuperhero names: \n")
for i in names :
    
    print(generate_superhero_name(i))

print("\n")