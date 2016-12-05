#!/usr/bin/env python
import random


class PetShop(object):
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory, we can set it at will."""
        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using abstract factory"""
        pet = self.pet_factory.get_pet()
        print "We have a lovely {}".format(pet)
        print "It says {}".format(pet.speak())
        print "We also have {}".format(self.pet_factory.get_food())


# Stuff that our factory makes
class Dog(object):
    def speak(self):
        return "wolf"

    def __str__(self):
        return "Dog"

    __repr__ = __str__


class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

    __repr__ = __str__


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper factory
def get_factory():
    """Let's be dynamic"""
    return random.choice([DogFactory, CatFactory])()


if __name__ == '__main__':
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print "=" * 20