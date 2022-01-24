#Name: Frank Shang
#Date: 07/21/2021
#Project 6D
#Description: This program contains a recursive function that solves a row of squares.

def row_puzzle(row, index=0, counter=None, last_value=0):
    '''recursive function that uses memoization to hold a dictionary that counts whether move is left or right. right is +1 and left is -1'''
    if counter is None:
        counter = {}

    if index not in counter:  # initializes the counter for each index in row to 0 if the index is not found
        counter[index] = 0

    if row[index] == 0:  # Base Case
        return True

    if counter[index] >= 3 or counter[index] <= -3:
        return False

    if index - row[index] < 0:
        counter[index] += 1
        return row_puzzle(row, index + row[index], counter, row[index])

    if index + row[index] >= len(row):
        counter[index] -= 1
        return row_puzzle(row, index - row[index], counter, row[index])

    # moves last index to the right by the last row[index] amount
    if counter[index] == -1:
        return row_puzzle(row, index + last_value + last_value, counter, row[index])

    # moves last index to the left by the last row[index] amount
    if counter[index] == 1:
        return row_puzzle(row, index - last_value - last_value, counter, row[index])

    # default move is to the right
    counter[index] += 1
    return row_puzzle(row, index + row[index], counter, row[index])

#row = [2, 4, 5, 3, 1, 3, 1, 4, 0]
#row2 = [1, 3, 2, 1, 3, 4, 0]
#print(row_puzzle(row))
