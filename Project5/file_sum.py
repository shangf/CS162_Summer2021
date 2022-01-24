# Name: Frank Shang
# Date: 07/14/2021
# Project 5A
# Description: This program reads a text file with numbers and writes the sum to an output file.

def file_sum(file):
    '''function that takes as a parameter the name of a text file that contains a list of numbers. returns the sum of the values to a text file named sum.txt'''
    total = 0.0
    with open(file, 'r') as inputFile:
        for line in inputFile:
            total += float(line)

    print("The sum is", total)

    with open('sum.txt', 'w') as outputFile:
        outputFile.write(str(total))

    print("Data written to sum.txt")
