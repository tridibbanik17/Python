# Test string
string = "Hello World!"

# String methods are like functions and they act on an object and transform the object in some way. They are called using dot notation, which means you write the name of the string, followed by a dot, and then the name of the method you want to use.
# For example, in this example, string is the object, and upper() is the method that we are calling on the string. The upper() method will return a new string that is the same as the original string, but with all the letters converted to uppercase.
# Convert the string to uppercase
string.upper()  # Output: 'HELLO WORLD!'

# The lower() method will return a new string that is the same as the original string, but with all the letters converted to lowercase.
# Convert the string to lowercase
string.lower()  # Output: 'hello world!'

# The title() method will return a new string that is the same as the original string, but with the first letter of each word capitalized and the rest of the letters in lowercase.
# Convert the string to title case    
string.title()  # Output: 'Hello World!'

# The capitalize() method will return a new string that is the same as the original string, but with the first letter of the string capitalized and the rest of the letters in lowercase.
# Capitalize the first letter of the string   
string.capitalize()  # Output: 'Hello world!'

string_to_strip = "   Hello World!   "
# The strip() method will return a new string that is the same as the original string, but with any leading and trailing whitespace removed.
# Remove leading and trailing whitespace from the string
string_to_strip.strip()  # Output: 'Hello World!'

# The split() method will return a list of substrings that are separated by a specified delimiter. By default, the delimiter is a space character.
# Split the string into a list of words 
string.split()  # Output: ['Hello', 'World!']

# The count() method will return the number of occurrences of a specified substring in the string.
# Count the number of occurrences of the letter 'o' in the string 
string.count('o')  # Output: 2

# The find() method will return the index of the first occurrence of a specified substring in the string. If the substring is not found, it will return -1.
# Find the index of the first occurrence of the letter 'o' in the string
string.find('o')  # Output: 4

# The index() method is similar to the find() method, but it will raise a ValueError if the specified substring is not found in the string.
# Find the index of the first occurrence of the letter 'o' in the string
string.index('o')  # Output: 4

############## The main difference between find() and index() in Python is how they handle a missing substring: find() returns -1, while index() raises a ValueError.

numeric_string = "12345"

# The isnumeric() method will return True if all characters in the string are numeric characters, and False otherwise. Numeric characters include digits, but also include other characters such as fractions and superscripts.
# Check if the string is a numeric string 
numeric_string.isnumeric()  # Output: True

# The isalpha() method will return True if all characters in the string are alphabetic characters, and False otherwise.
# Check if the string is an alphabetic string 
string.isalpha()  # Output: False

# The len() function will return the number of characters in the string, including spaces and punctuation. It is not a method of the string object, but rather a built-in function that can be used with any iterable object, including strings.
# A space is considered a character, and the exclamation mark is also considered a character, so the total number of characters in the string is 12.
len(string)  # Output: 12

# Get the first character of the string in two ways.
string[0]  # Output: 'H'
string[-12]  # Output: 'H'

# Get the last character of the string in two ways.
string[11]  # Output: '!'
string[-1]  # Output: '!'

# string[12]  # This will raise an IndexError because the index is out of range.
# string[-13]  # This will also raise an IndexError because the index is out of range.

# Get a substring or a slice from the string.
string[0:5]  # Output: 'Hello'

# Get a substring from beginning to a specific index.
string[:5]  # Output: 'Hello'

# Get a substring from a specific index to the end of the string.
string[5:]  # Output: ' World!'

# [start:stop:step]
# Get every second character from the string, starting from the first character (index 2, inclusive) and ending at the 12th character (exclusive).
string[2:12:2]  # Output: 'loWrd'

# Get every second character from the string, starting from the first character (index 0, inclusive) and ending at the 12th character (exclusive).
string[::2]  # Output: 'HloWrd'

# Get the string in reverse order.
string[::-1]  # Output: '!dlroW olleH'

