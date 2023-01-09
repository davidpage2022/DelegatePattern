"""
An animal in the wild.

The class below should be mostly familiar based on what we learned in class.

You may notice that the "behaviour" parameter of __init__ is an object of
type AnimalBehaviour. Using it, we can call any function or variable that
are defined inside AnimalBehaviour, such as:

    behaviour.handle_forage(animal)

Where animal is an object of class Animal. This causes the animal to attempt to
forage for food.

After studying the code, proceed to review animal_behaviour (if you haven't already).

DO NOT MODIFY THIS FILE.
"""


class Animal:
    """Describes an animal in the wild."""

    def __init__(self, name, behaviour, gestation_period=0, starting_hunger=0.5, starting_gestation=0):
        """Construct an animal with customisable behaviour.

        :param name: Name of the type of animal (e.g. "Lion").
        :param behaviour: Object of type derived from (a child of) AnimalBehaviour
        that defines the animal's behaviour and response to time passing.
        :param starting_hunger: Hunger level to start with,
        where 0.0 is not hungry and 1.0 is nearing starvation."""
        self.name = name
        self.behaviour = behaviour
        self.gestation_period = gestation_period
        self.hunger = starting_hunger
        self.is_alive = True
        self.days_lived = 0
        self.is_pregnant = False
        self.days_gestation = starting_gestation
        self.is_postpartum = False

    def __repr__(self):
        string = f"{self.name} (is_alive: {self.is_alive}, is_pregnant: {self.is_pregnant}, " \
                 f"days pregnant: {self.days_gestation}, hunger: {self.hunger:.2f})"
        return f"{string:45}"

    def simulate(self, days_passed, animals):
        """Simulate the animal in the wild with other animals.

        :param days_passed: Number of days to simulate.
        :param animals: List of all animals in the environment."""
        behaviour = self.behaviour

        # Do nothing if the animal is dead.
        if not self.is_alive:
            return

        # Attempt to hunt for an animal (excluding self and dead animals).
        other_animals = [animal for animal in animals if animal is not self and animal.is_alive]
        animal_caught = behaviour.handle_hunt(self, other_animals)
        if animal_caught:
            behaviour.handle_eat(self, animal_caught)

        # Attempt to forage for plant food.
        food_found = behaviour.handle_forage(self)
        if food_found:
            behaviour.handle_eat(self)

        # Manage breeding
        is_pregnant = behaviour.set_as_pregnant(self)
        if is_pregnant:
            self.days_gestation += days_passed
        if self.days_gestation == self.gestation_period:
            behaviour.give_birth(self)
            if self.is_postpartum:
                offspring = Animal(self.name, self.behaviour, self.gestation_period)
                animals.append(offspring)
                self.is_postpartum = False
                return animals

        # Handle response to time passing.
        self.days_lived += days_passed
        for i in range(days_passed):
            behaviour.handle_day_passed(self)
