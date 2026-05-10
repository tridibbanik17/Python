# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# O(n^2)
def contain_duplicates_n2(nums) -> bool:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# O(nlogn)
def contain_duplicates_nlogn(nums) -> bool:
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]:
            return True
    return False

# O(n)
def contain_duplicates_n(nums) -> bool:
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False

print(contain_duplicates_n2([1,2,3,1]))
print(contain_duplicates_nlogn([1,2,3,1]))
print(contain_duplicates_n([1,2,3,1]))