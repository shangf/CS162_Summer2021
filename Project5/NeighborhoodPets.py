# Name: Frank Shang
# Date: 07/14/2021
# Project 5D
# Description: This program loads data from a JSON file and uses it to return a set of all pet species. It allows the user to write and save a JSON file as well.

import json

class NeighborhoodPets():

    def __init__(self):
        '''init method that initalizes all data members'''
        self._pets = {}

    def add_pet(self, name, species, owner):
        '''takes as parameters the name of the pet, the species of the pet, and the name of the pet's owner. if a pet has the same name as a pet that has already been added, then the function should not add the new pet'''
        if name in self._pets:
            print("Can not add two pets with the same name.")
        else:
            self._pets[name] = [species, owner]

    def delete_pet(self, name):
        '''takes as a parameter the name of the pet and deletes that pet'''
        if name in self._pets:
            self._pets.pop(name, None)
            print(name, "deleted from data.")
        else:
            print(name, "not found.")

    def get_owner(self, name):
        '''takes as a parameter the name of the pet and returns the name of its owner'''
        if name not in self._pets:
            print(name, "not found.")
        else:
            return self._pets[name][1]

    def save_as_json(self, filename):
        '''takes as a parameter the name of the file and saves it in JSON format with that name'''
        with open(filename, 'w') as outputFile:
            json.dump(self._pets, outputFile)

    def read_json(self, filename):
        '''takes as a parameter the name of the file to read and loads that file. replaces all of the pets currently in memory'''
        with open(filename, 'r') as inputFile:
            self._pets.clear()
            self._pets = json.load(inputFile)

    def get_all_species(self):
        '''takes no parameters and returns a set of the species of all pets'''
        species_list = []
        for key in self._pets:
            species_list.append(self._pets[key][0])
        species_set = set(species_list)
        print(species_set)
        return species_set
