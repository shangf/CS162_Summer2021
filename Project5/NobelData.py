# Name: Frank Shang
# Date: 07/14/2021
# Project 5B
# Description: This program reads a json file containing data on Nobel Prizes. It allows the user to search the data and returns a sorted list of the surnames for the winners.


import json


class NobelData():

    def __init__(self):
        '''init method that reads the json file'''
        self._dict = {}
        with open('nobels.json', 'r') as inputFile:
            self._dict = json.load(inputFile)

    def search_nobel(self, year, category):
        '''takes as parameters a year and a category. returns a sorted list of the surnames for the winners'''
        surnames = []
        for count in range(0, len(self._dict['prizes'])):
            if self._dict['prizes'][count]['year'] == year and self._dict['prizes'][count]['category'] == category:
                for index in range(0, len(self._dict['prizes'][count]['laureates'])):
                    print(self._dict['prizes'][count]['laureates'][index]['surname'])
                    surnames.append(self._dict['prizes'][count]['laureates'][index]['surname'])
        surnames.sort()
        return surnames
