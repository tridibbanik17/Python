# Immutable
# Cannot alter order of items in a tuple

my_tuple = (1, 2, 3)
print(my_tuple) # Output: (1, 2, 3)

print(my_tuple[0]) # Output: 1 - Accessing the first element of the tuple using indexing

print(my_tuple[-1]) # Output: 3 - Accessing the last element of the tuple using negative indexing

# my_tuple[0] = 4 # TypeError: 'tuple' object does not support item assignment - trying to change the value of an element in the tuple will raise an error

coordinates = (10, 20) # (latitude, longitude)
print(coordinates) # Output: (10, 20)

latitude, longitude = coordinates # Unpacking the tuple into separate variables
print(f"Latitude: {latitude}, Longitude: {longitude}") # Output: Latitude: 10, Longitude: 20