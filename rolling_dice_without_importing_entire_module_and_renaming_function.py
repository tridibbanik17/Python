# importing only the required function from the random module and renaming the function to random_int
from random import randint as random_int

die_1 = random_int(1, 6)  # Generate a random integer between 1 and 6 for the first die
die_2 = random_int(1, 6)  # Generate a random integer between 1 and 6 for the second die

total = die_1 + die_2  # Calculate the total of the two dice

print(f"You rolled a {die_1} and a {die_2}. Total: {total}")  # Print the results of the dice rolls and the total