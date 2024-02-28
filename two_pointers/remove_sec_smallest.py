def remove_second_smallest(array):
    array.sort()
    array.remove(array[1])
    return array

array = [1, 2, 3, 4, 5]
print(remove_second_smallest(array))



def remove_second_smallest(nums):
    """
    Removes the second smallest element from an array.
    Args:
        nums: A list of integers.
    """

    # Find the smallest element in the array.
    smallest = min(nums)

    # Find the second smallest element in the array.
    second_smallest = float('inf')
    for num in nums:
        if num < second_smallest and num != smallest:
            second_smallest = num

    # Remove the second smallest element from the array.
    nums.remove(second_smallest)

# Example usage:

nums = [2, 3, 1, 5, 4]
remove_second_smallest(nums)
print(nums)


