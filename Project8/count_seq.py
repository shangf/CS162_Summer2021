# Name: Frank Shang
# Date: 07/30/2021
# Project 8A
# Description: This program contains a generator function that generates a counting sequence.

def count_seq():
    '''
    generator function that treats the first two terms as special cases
    if not the first two cases, calls find_count function to find the next counting sequence
    '''
    counter = 0
    while True:
        if counter == 0:
            string = '2'
            yield string
            counter += 1
        if counter == 1:
            string = '12'
            yield string
            counter += 1
        else:
            next_sequence = find_count(string)
            string = next_sequence
            yield string

def find_count(string):
    '''
    function that traverses through the string and keeps a count of the current letter (number as a string)
    '''
    previous = ''
    while len(string) > 0:
        counter = 0
        first_number = string[0]
        for letter in string:
            if letter == first_number:
                counter += 1
            else:
                break
        next_sequence = previous + str(counter) + str(first_number)
        previous = next_sequence
        if len(string) - counter == 0:
            return next_sequence
        else:
            next_string = string[counter:]
            string = next_string
    return next_sequence

#gen = count_seq()

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
