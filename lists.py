letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

letters[0] = 'A'  # Change the first element to 'A'
print(letters)

print(letters[0])  # Print the first element, which is now 'A'

print(letters[-1])  # Print the last element, which is 'e'

# print(letters[20])  # This will raise an IndexError because the index is out of range

print(letters[0:3])  # Print the first three elements, which are ['A', 'b', 'c']

print(letters[:3])  # Print the first three elements, which are ['A', 'b', 'c']

print(letters[::2])  # Print every other element, which are ['A', 'c', 'e']

print(letters[::-1])  # Print the list in reverse order, which are ['e', 'd', 'c', 'b', 'A']

print(len(letters))  # Print the number of elements in the list, which is 5

print(list())  # Print an empty list, which is []

print(list('hello'))  # Print a list of the characters in the string 'hello', which are ['h', 'e', 'l', 'l', 'o']

letters = ['a', 'b', 'c', 'd']

letters2 = letters  # This creates a reference to the same list, not a copy
letters.append('e')  # This will modify the original list that letters2 also references
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e']
print(letters2)  # Output: ['a', 'b', 'c', 'd', 'e'] because letters2 references the same list as letters

letters3 = list(letters)  # This creates a new list that is a copy of the original list
letters.append('f')  # This will modify the original list that letters3 does not reference
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
print(letters3)  # Output: ['a', 'b', 'c', 'd', 'e']

nested_list = [[1,2,3],
               [4,5,6],
               [7,8,9]]
print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nested_list[1][0] = 1000

print(nested_list)  # Output: [[1, 2, 3], [1000, 5, 6], [7, 8, 9]]