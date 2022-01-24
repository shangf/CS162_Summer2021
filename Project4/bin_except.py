# Name: Frank Shang
# Date: 07/09/2021
# Assignment 4A
# Description: This program is a modified version of the Exploration's Binary Search algorithm.
# If the searched for value is not in the list, the function raises an Exception instead of returning -1.


class TargetNotFound(Exception):
  """
  class that inherits from the Exception class
  """
  pass

def bin_except(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, raises a TargetNotFound exception, indicating the target value isn't in the list
  """

  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  if target != a_list[middle]:
    raise TargetNotFound


if __name__ == '__main__':
  try:
    my_list = [123, 325, 3522, 324323]
    target = 326
    index = bin_except(my_list, target)
  except TargetNotFound:
    print("Target not found.")
  else:
    print(target, "found at index", index)
