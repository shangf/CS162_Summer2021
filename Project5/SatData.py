# Name: Frank Shang
# Date: 07/14/2021
# Project 5C
# Description: This program reads a JSON file containing 2010 SAT results for New York City and creates a csv file based on the data.

import json


class SatData():

    def __init__(self):
        '''init method that reads the file'''
        with open('sat.json', 'r') as inputFile:
            self._dict = json.load(inputFile)

    def save_as_csv(self, DBN_list):
        '''takes as a parameter a list of DBNs and saves a CSV file'''
        comma = ','
        DBN_list.sort()
        with open('output.csv', 'w') as outputFile:
            outputFile.write(
                'DBN' + comma + 'School Name' + comma + 'Number of Test Takers' + comma + 'Critical Reading Mean' + comma + 'Mathematics Mean' + comma + 'Writing Mean' + '\n')
            for dbn in DBN_list:
                for count in range(0, len(self._dict['data'])):
                    if self._dict['data'][count][8] == dbn:
                        outputFile.write(dbn + comma)
                        for index in range(9, 13):
                            if comma in self._dict['data'][count][index]:
                                self._dict['data'][count][index] = '"' + self._dict['data'][count][index] + '"'
                                outputFile.write(self._dict['data'][count][index] + comma)
                            else:
                                outputFile.write(self._dict['data'][count][index] + comma)
                        outputFile.write(self._dict['data'][count][13])
                outputFile.write('\n')
