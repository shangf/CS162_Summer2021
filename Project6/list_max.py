# Name: Frank Shang
# Date: 07/19/2021
# Project 6A
# Description: This program uses a recursive function to find the maximum number within a list.

def list_max(a_list):
    '''helper function that sets the maximum to the first element in the list, then calls recursion function'''
    max = a_list[0]
    return rec_list_max(a_list, max, 1)

def rec_list_max(a_list, max, pos):
    '''recursive function that finds and returns the max'''
    if pos == len(a_list):
        return max
    if a_list[pos] > max:
        return rec_list_max(a_list, (max - max) + a_list[pos], pos + 1)
    else:
        return rec_list_max(a_list, max, pos + 1)

#my_list = [22223, 42, 697, 3465]
#print(list_max(my_list))
