import json
import random
import string

# List of animal names
animals = ["cat", "dog", "lion", "tiger", "elephant", "giraffe", "zebra", "monkey", "panda", "koala", "kangaroo", "bear", "fox", "wolf", "deer", "rabbit", "horse", "cow", "sheep", "goat"]

# List of character names
characters = ["mario", "luigi", "peach", "toad", "yoshi", "bowser", "wario", "waluigi", "dk", "diddy", "zelda", "link", "ganon", "kirby", "meta-knight", "pikachu", "charizard", "mewtwo", "sonic", "tails"]

# List of people names
people = ["emma", "olivia", "ava", "isabella", "sophia", "mia", "charlotte", "amelia", "harper", "evelyn", "abigail", "emily", "elizabeth", "victoria", "madison", "michael", "james", "william", "jacob", "john"]

# Generate email and password combinations
data = []
for i in range(20):
    animal_name = random.choice(animals)
    character_name = random.choice(characters)
    person_name = random.choice(people)
    digits = ''.join(random.choices(string.digits, k=4))
    password = animal_name + character_name + person_name + digits
    email = f"{person_name}.{random.choice(string.ascii_lowercase)}@example.com"
    data.append({"email": email, "password": password})

# Write to JSON file
with open("email_passwords.json", "w") as f:
    json.dump(data, f, indent=4)
