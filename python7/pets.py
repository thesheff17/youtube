#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Dan Sheffner Digital Imaging Software Soltuions, INC
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# I give credit to https://ace.c9.io/#nav=about for this web based text editor

# my source code can be found here for this class
# https://raw.githubusercontent.com/thesheff17/youtube/master/python7/pets.py

"""
This program will demo a class in python
"""

import random

class Pets(object):
    """
    This class will represent a class for pets
    """

    version = '0.1'

    def __init__(self, name, owner):
        """
        creates the variables associated with the class

        :type name: string
        :param name: the name of the pet
        
        :type owner: string
        :param owner: the owner of the pet
        """

        self.name = []
        self.owner = owner
        self.name.append(name)

    def add_pet(self, name):
        """
        adds a pet to the pet list

        :type name: string
        :param name: pet name to add to the list
        """

        self.name.append(name)

    def show_pets(self):
        """
        prints out all the pets in the list
        """

        print ("The owner of these pets are: " + self.owner)
        for each in self.name:
            print (each)

    @classmethod            # alternative constructor
    def random_pets(cls, owner):
        """
        special method was created after to address owners that did not 
        want to pick a pet name.

        :type cls: Pets
        :param cls: an instance of the class passed to __init__

        :type owner: string
        :param owner: the owner of this pet
        """

        pets_random = ['Cocoa', 'Jasper', 'Elmo', 'Chester', 'Rufus']
        random_pet_name = random.choice(pets_random)
        return cls(random_pet_name, owner)

    @staticmethod           # attach a method doesn't need self
    def get_average_age(pet_type):
        """
        prints out the average age of a pet

        :type pet_type: string
        :param pet_type: 3 most popular pets
         """

        if pet_type is 'dog':
            print ('Dogs average life is: 13 years')
        if pet_type is 'cat':
            print ('Cats average life is: 15 years')
        if pet_type is 'fish':
           print ('Gold Fish average life is: 30 years')


if __name__ == "__main__":
    # the first class
    p1 = Pets('jabba', 'Dan Sheffner')
    print(type(p1))
    p1.show_pets()
    print ()
    p1.get_average_age('cat')

    print ()

    # the second class
    p2 = Pets.random_pets('Chris Sheffner')
    print(type(p2))
    p2.show_pets()
    print ()

   # owner gets another pet later on and names it roo
    print ('owner buys another pet later on...')
    p2.add_pet('Roo')
    p2.show_pets()
    print ()

    p2.get_average_age('dog')
    p2.get_average_age('fish')
