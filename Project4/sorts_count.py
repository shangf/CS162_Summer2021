# Name: Frank Shang
# Date: 07/09/2021
# Assignment 4D
# Description: This program counts the number of comparisons and exchanges in a bubble sort or an insertion sort.


def bubble_count(a_list):
  """
  uses bubble sort to sort the list in ascending order. counts the number of comparisons and exchanges.
  returns as a tuple in the order of comparisons, exchanges
  """
  comparisons = 0
  exchanges = 0
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      comparisons += 1
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp
        exchanges += 1

  tup = (comparisons, exchanges)
  return tup

def insertion_count(a_list):
  """
  uses insertion sort to sort the list in ascending order. counts the number of comparisons and exchanges.
  returns as a tuple in the order of comparisons, exchanges
  """
  comparisons = 0
  exchanges = 0
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      comparisons += 1
      a_list[pos + 1] = a_list[pos]
      exchanges += 1
      pos -= 1
    a_list[pos + 1] = value
  tup = (comparisons, exchanges)
  return tup
