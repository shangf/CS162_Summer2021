# Name: Frank Shang
# Date: 07/20/2021
# Project 6C
# Description: This program contains a recursive function that determines if a string is a subsequence of another string.


def is_subsequence(string1, string2):
    '''helper function that determines the lengths of the first string and second string'''
    str1_len = len(string1)
    str2_len = len(string2)
    return rec_is_subsequence(string1, string2, str1_len, str2_len)


def rec_is_subsequence(string1, string2, len1, len2):
    '''recursive function that uses each string's length to determine whether string1 is in string2'''
    if len1 == 0:
        return True
    if len2 == 0:
        return False
    if string1[len1 - 1] == string2[len2 - 1]:
        return rec_is_subsequence(string1, string2, len1 - 1, len2)
    else:
        return rec_is_subsequence(string1, string2, len1, len2 - 1)

# print(is_subsequence("hez", "ahoepalm"))
