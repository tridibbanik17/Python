# Prompt the user to provide missing words for the Mad Libs story

# Get user input for the missing words
colour = input("Enter a colour: ").strip().upper()  # Remove leading and trailing whitespace from the input and convert it to uppercase
adjective = input("Enter an adjective: ").strip().upper()  # Remove leading and trailing whitespace from the input and convert it to uppercase

text = f"""
Roses are {colour},
Violets are blue,
Sugar is {adjective},
And so are you!
"""
# Print the completed Mad Libs story
print(text)