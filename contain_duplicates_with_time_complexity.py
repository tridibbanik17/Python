# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# O(n^2)
import time
import random
nums = list(range(10000))
random.shuffle(nums)  # defeats Timsort's optimization
nums.append(9999)     # duplicate at the end, but shuffled so it's hard to find
def contain_duplicates_n2(nums):
    start = time.time()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                end = time.time()
                print(f"Time taken: {end - start} seconds")
                return True
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    return False

print(contain_duplicates_n2(nums))
                          
# O(nlogn)
def contain_duplicates_nlogn(nums):
    start = time.time()
    nums.sort()  # Sort the array in-place
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:  # Check if the current element is the same as the previous one
            end = time.time()
            print(f"Time taken: {end - start} seconds")
            return True
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    return False

print(contain_duplicates_nlogn(nums))

# O(n)
def contain_duplicates_n(nums):
    start = time.time()
    seen = set()  # Create an empty set to store seen numbers
    for num in nums:
        if num in seen:  # Check if the number is already in the set
            end = time.time()
            print(f"Time taken: {end - start} seconds")
            return True
        seen.add(num)  # Add the number to the set
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    return False

print(contain_duplicates_n(nums))
