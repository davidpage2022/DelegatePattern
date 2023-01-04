"""
How animals behave.

Study the code and notes below, then when you are ready, proceed to animal_tests.py.

---------------------------------------------------------------------------

Terminology:

Here is some terminology we will be using.

There are a number of ways to describe class inheritance relationships:

- Child vs Parent         # Common. Easiest to understand.
- Derived vs Base         # Equivalent to child and parent. Commonly used in documentation.
- Subclass vs superclass  # Not common in Python.

A child class inherits from a parent class.

Also recall that an object is an instance of a class, like so:

    some_object = SomeClass()

---------------------------------------------------------------------------

Abstract Base Class:

You can see the lines "from abc import ABC, abstractmethod" and "@abstractmethod".
It's not important to understand these, but for your interest, "ABC" stands for "Abstract Base Class".
It means the class is only designed to be a parent class, not to be created on its own.
For example, the following is not allowed because AnimalBehaviour is an abstract base class:

    animal_behaviour = AnimalBehaviour(is_predator=False)  # Error! Cannot create instance of abstract class.

However, if we create a class that inherits from AnimalBehaviour...

    class ChildAnimalBehaviour(AnimalBehaviour):
        def __init__(self, **kwargs):
            super().__init__(**kworgs)

We can create an instance of that class:

    animal_behaviour = ChildAnimalBehaviour(is_predator=False)  # OK!
---------------------------------------------------------------------------

DO NOT MODIFY THIS FILE.

"""
from abc import ABC, abstractmethod


class AnimalBehaviour(ABC):
    """Describes how an animal in the wild behaves and responds to time passing.

    Create your own classes that derive from AnimalBehaviour to customise the behaviour."""

    @abstractmethod
    def __init__(self, hunger_increase_per_day=0.005):
        """Construct an animal behaviour.

        :param hunger_increase_per_day: Amount to increase hunger level per day."""
        self.hunger_increase_per_day = hunger_increase_per_day

    def __repr__(self):
        return self.__class__.__name__

    def handle_hunt(self, animal, other_animals):
        """Handle an animal hunting for another animal to eat in the wild.

        :param animal: The animal that is hunting.
        :param other_animals: A list of all animals (excluding the animal that is hunting).
        :returns: Returns the animal that was caught.
        If no animal was caught, returns None."""
        return None

    def handle_forage(self, animal):
        """Handle an animal foraging for plant food in the wild.

        :param animal: The animal that is foraging.
        :returns: Returns True if the animal found food, False otherwise."""
        return False

    def handle_eat(self, animal, animal_to_eat=None):
        """Handles an animal eating plant food or another animal.

        :param animal: The animal that is eating.
        :param animal_to_eat: The animal being eaten. Is None if the animal is eating plant food."""
        pass  # Do nothing by default.

    def handle_day_passed(self, animal):
        """Handles a single day passing for an animal.

        Call this method from the derived class to increase animal hunger.
        The animal will die of starvation if hunger exceeds 1.0.
        :param animal: The animal for which a day has passed."""
        animal.hunger += self.hunger_increase_per_day
        if animal.hunger > 1.0:
            animal.hunger = 1.0
            animal.is_alive = False
