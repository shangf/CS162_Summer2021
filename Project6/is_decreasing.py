# Name: Frank Shang
# Date: 07/19/2021
# Project 6B
# Description: This program uses a recursive function to determine whether the elements of a list are strictly decreasing.


def is_decreasing(a_list, pos = 0):
    '''recursive function that determines if the elements are strictly decreasing'''
    if pos == len(a_list) - 1:
        return True

    status = a_list[pos] > a_list[pos + 1]
    return is_decreasing(a_list, pos + 1) and status

#my_list = [10, 9, 37, 3, 1]
#print(is_decreasing(my_list))
