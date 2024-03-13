#removing the second smallest value

def second_smallest(values):
    values.sort()
    values.pop(1)
    return values

print(second_smallest([40,30,100,80]))


def remove_second_smallest(array):
  """Removes the second smallest number from an array that is not sorted in place.

  Args:
    array: A list of numbers.

  Returns:
    A list of numbers with the second smallest number removed.
  """

  # Find the smallest and second smallest numbers in the array.
  smallest = min(array)
  second_smallest = float('inf')
  for number in array:
    if number < second_smallest and number != smallest:
      second_smallest = number

  # Remove the second smallest number from the array.
  array.remove(second_smallest)

  # Return the array with the second smallest number removed.
  return array

# Example usage:

array = [5, 3, 2, 1, 4]
print(remove_second_smallest(array))
