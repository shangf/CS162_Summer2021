# Name: Frank Shang
# Date: 07/09/2021
# Assignment 4C
# Description: This program uses the insertion sort from the Exploration to sort strings, ignoring case.


def string_sort(string_list):
  """sorts a list of strings in ascending order, ignoring case"""
  for index in range(1, len(string_list)):
    string = string_list[index]
    string_caps = string_list[index].upper()
    position = index - 1
    while position >= 0 and string_list[position].upper() > string_caps:
      string_list[position + 1] = string_list[position]
      position -= 1
    string_list[position + 1] = string
