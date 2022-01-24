# Name: Frank Shang
# Date: 07/30/21
# Project 8b
# Description: This program uses a decorator function named sort_timer to compare
# the times of bubble sort vs. insertion sort.

import time
import random
import functools
from matplotlib import pyplot

def sort_timer(func):
    '''
    decorator function that times either the bubble sort or insertion sort
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beg_time = time.perf_counter()
        print("Calling", func.__name__)
        func(*args, **kwargs)
        print("Sorting finished.")
        end_time = time.perf_counter()
        timing = end_time - beg_time
        print("Total time:", timing)
        return timing

    return wrapper

@sort_timer
def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

def compare_sorts(bubble, insertion):
    '''
    function that creates a list of random numbers in intervals of 1000, up to 10000
    calls the bubble and insertion methods to time sorting
    prints out a graph that displays the information
    red: bubble sort
    green: insertion sort
    '''
    bubble_x = []
    bubble_y = []
    insertion_x = []
    insertion_y = []
    count = 0
    while count != 10:
        size = 1000 * (count + 1)
        list_one = []
        while len(list_one) != size:
            list_one.append(random.randint(1, 10000))
        list_two = list(list_one)
        bubble_x.append(size)
        bubble_y.append(bubble(list_one))
        insertion_x.append(size)
        insertion_y.append(insertion(list_two))
        count += 1
    print("Red: Bubble Sort")
    print("Green: Insertion Sort")

    pyplot.plot(bubble_x, bubble_y, 'ro--', linewidth=2)
    pyplot.plot(insertion_x, insertion_y, 'go--', linewidth=2)
    pyplot.xlabel("number of elements sorted")
    pyplot.ylabel("time in seconds")
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
