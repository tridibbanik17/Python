# Cannot contain duplicate items
# Unordered

my_set = {1,2,3,4,5}
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set = {1,2,2,3,4,5,5} # set removes duplicates
print(my_set) # Output: {1, 2, 3, 4, 5}

# Convert list to set
print(set([1,2,2,3,3,3,4,5])) # Output: {1, 2, 3, 4, 5}

# intersection of two sets
prime = {2,3,5,7}
odd = {1,3,5,7,9}
intersection = prime & odd
print(intersection)

# union of two sets
union = prime | odd
print(union)

# difference of two sets
diff = prime - odd
print(diff)