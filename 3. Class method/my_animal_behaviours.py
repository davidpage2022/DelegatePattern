"""
Animal behaviours.

Here we see two different types of animal behaviours that are children of AnimalBehaviour:

    HerbivoreBehaviour: This is a complete example to illustrate creating animal behaviours.
    CarnivoreBehaviour: It will be your job to complete this class.

But first a word about method overriding and polymorphism...

---------------------------------------------------------------------------

Method Overriding and Polymorphism

Method overriding means you have a method in a parent class that you override with a method
in the child class with the same name. For example:

    class Parent:
        def do_something():
            print("I am the parent")

    class Child
        def do_something():
            print("I am the child")

Now let's see what happens if we create instances of those classes:

    parent = Parent()
    parent.do_something()  # Output: I am the parent

    child = Child()
    child.do_something()  # Output: I am the child

But now consider this code:

    things = [Child(), Parent(), Child()]
    for thing in things:
        thing.do_something()

What do you expect the output to be. It is:

    I am the child    # Child.do_something()
    I am the parent   # Parent.do_something()
    I am the child    # Child.do_something()

We can treat different objects the same, even though they are different types!
This works because Child inherits from Parent.
This is what is known as polymorphism.

This can be a complex topic so I recommend researching "python polymorphism" and
"python method overriding".

In the code below notice that we don't need to have a docstring for methods
that override a function in the parent class.

---------------------------------------------------------------------------

The Exercise

When you're ready your exercise is to complete the CarnivoreBehaviour class.

It should override the following methods:

- __init__: Pass on keyword arguments to the parent constructor.
            Add your own parameters as needed. You may need to update
            animal_tests.py with the new parameters.
- handle_hunt: Randomly choose an animal to catch (return),
            with a chance that no animal will be caught (return None).
            The chance the hunter will catch prey should be a parameter
            passed in to the constructor.
- handle_eat: Decrease the animal's hunger and kill the animal that was caught
            (is_alive = False).
- handle_day_passed: Handle chance that the animal will die of starvation
            by calling the parent handle_day_passed() method.
            Handle the chance of dying of old age, but have the carnivore
            live shorter than the herbivore.

Refer to animal_tests.py for expected output.

"""
import random

from animal_behaviour import AnimalBehaviour


class HerbivoreBehaviour(AnimalBehaviour):
    """Describes the behaviour of a plant-eating animal."""
    HUNGER_DECREASE_ON_EAT = 0.08
    CHANCE_TO_DIE_OF_AGE_PER_DAY_LIVED = 0.00018

    def __init__(self, chance_to_find_food=0.1, **kwargs):
        """ Construct a herbivore behaviour. Inherited from AnimalBehaviour.

        :param chance_to_find_food: The chance to find food in the environment per day
        (0 is no chance, 1 is guaranteed).
        :param kwargs: Captures all the keyword arguments from the parent.
        """
        super().__init__(**kwargs)  # Pass on keyword arguments to AnimalBehaviour.__init__().
        self.chance_to_find_food = chance_to_find_food

    def handle_forage(self, animal):  # Overrides AnimalBehaviour.handle_forage().
        found_food = (random.uniform(0.0, 1.0) <= self.chance_to_find_food)
        return found_food

    def handle_eat(self, animal, animal_to_eat=None):  # Overrides AnimalBehaviour.handle_eat().

        # Check that we are not trying to eat an animal.
        if animal_to_eat:
            print(f"Error: {animal.name.title()} cannot eat another animal")
            return

        # Decrease hunger.
        animal.hunger -= self.HUNGER_DECREASE_ON_EAT
        if animal.hunger < 0.0:
            animal.hunger = 0.0

    def handle_day_passed(self, animal):  # Overrides AnimalBehaviour.handle_day_passed().

        # Call the handle_day_passed() in the parent to increase hunger and handle death by starvation.
        super().handle_day_passed(animal)

        # TODO: Remove dying of old age as not relevant to simulation?

        # Handle chance to die of old age.
        chance_to_die = animal.days_lived * self.CHANCE_TO_DIE_OF_AGE_PER_DAY_LIVED
        random_chance = random.uniform(0.0, 1.0)
        if random_chance <= chance_to_die:
            animal.is_alive = False


class CarnivoreBehaviour(AnimalBehaviour):
    """Describes the behaviour of a meat-eating animal."""
    HUNGER_DECREASE_ON_EAT = 0.2  # Higher level of decrease than for herbivores
    CHANCE_TO_DIE_OF_AGE_PER_DAY_LIVED = 0.00018  # Higher daily chance of death than for herbivores


    def __init__(self, chance_to_find_food=0.05, chance_to_catch_prey=0.2, **kwargs):
        """ Construct a carnivore behaviour. Inherited from AnimalBehaviour."""
        super().__init__(**kwargs)  # Pass on keyword arguments to AnimalBehaviour.__init__().
        self.chance_to_find_food = chance_to_find_food
        self.chance_to_catch_prey = chance_to_catch_prey

    def handle_hunt(self, animal, other_animals):  # Overrides AnimalBehaviour.handle_hunt()
        """Handle an animal hunting for another animal to eat in the wild.

        :param animal: The animal that is hunting.
        :param other_animals: A list of all animals (excluding the animal that is hunting).
        :returns: Returns the animal that was caught.
        If no animal was caught, returns None."""
        if random.uniform(0.0, 1.0) <= self.chance_to_catch_prey:
            animal_to_eat = other_animals[random.randint(0, (len(other_animals) - 1))]
            return animal_to_eat
        else:
            return None

    def handle_eat(self, animal, animal_to_eat=None):  # Overrides AnimalBehaviour.handle_eat()
        """Handles an animal eating another animal.

        :param animal: The animal that is eating.
        :param animal_to_eat: The animal being eaten. Is None if the animal is eating plant food."""
        animal.hunger -= self.HUNGER_DECREASE_ON_EAT
        if animal.hunger < 0.0:
            animal.hunger = 0.0
        if animal_to_eat.is_alive:
            animal_to_eat.is_alive = False
            return animal_to_eat.is_alive
        else:
            pass  # Do nothing by default.

    def handle_day_passed(self, animal):  # Overrides AnimalBehaviour.handle_day_passed
        """Handles a single day passing for an animal.

        Call this method from the derived class to increase animal hunger.
        The animal will die of starvation if hunger exceeds 1.0.
        :param animal: The animal for which a day has passed."""
        super().handle_day_passed(animal)
        chance_to_die = animal.days_lived * self.CHANCE_TO_DIE_OF_AGE_PER_DAY_LIVED
        random_chance = random.uniform(0.0, 1.0)
        if random_chance <= chance_to_die:
            animal.is_alive = False
