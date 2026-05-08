# Get two random numbers between 1 and 6, inclusive, to simulate rolling two dice
import random

############### random is a built-in module in Python, which is random.py file that can be found using this command in the terminal: python -c "import random; print(random.__file__)"

die1 = random.randint(1, 6)  # Generate a random integer between 1 and 6 for the first die
die2 = random.randint(1, 6)  # Generate a random integer between 1 and 6 for the second die

# Calculate the total of the two dice
total = die1 + die2  # Calculate the total of the two dice

# print(random.randrange(1, 7))  # This will also generate a random integer between 1 and 6, but it is less commonly used for simulating dice rolls because it is less intuitive than randint().

# Print the results of the dice rolls and the total
print(f"You rolled a {die1} and a {die2}. Total: {total}")  # Print the results of the dice rolls and the total

