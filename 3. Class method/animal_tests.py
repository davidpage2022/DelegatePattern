"""
In this file we test our animal behaviour classes out in the wild.

Notice that we create a CarnivoreBehaviour() and then pass it as the behaviour parameter when
creating an Animal. Likewise, we create a HerbivoreBehaviour with the specified chance_to_find_food
and then pass it into the behaviour parameter when creating an Animal.

We then run a simulation on all animals. Note that we didn't have to do any special behaviour
for lions as opposed to antelopes. All of the customised behaviour is defined inside
CarnivoreBehaviour and HerbivoreBehaviour, respectively. Because each animal has a reference
to a behaviour object, it knows which custom behaviour to use when we call animal.simulate().

---------------------------------------------------------------------------

Expected Output:

Each row represents the state of all animals at a point in the simulation.

When CarnivoreBehaviour is completed the output should show some lions feeding sometimes.
As a result, at least some should live past day 80.
A corresponding antelope should have is_alive equal False because a lion ate it.
You can tell a lion ate it because the antelope's hunger will be less than 1 when is_alive became False.

---------------------------------------------------------------------------

Advanced extension exercise:

TODO: I might do this myself?

Animals die. Add a way for them to birth new ones. Remember that lists can be modified from
inside a function.

"""
from animal import Animal
from my_animal_behaviours import HerbivoreBehaviour, CarnivoreBehaviour

NUMBER_OF_LIONS = 4
NUMBER_OF_ANTELOPES = 15
SIMULATE_MAX_DAYS = 100
SIMULATE_INTERVAL = 10


# Use these constants to test breeding:
# NUMBER_OF_LIONS = 1
# NUMBER_OF_ANTELOPES = 4
# SIMULATE_MAX_DAYS = 20
# SIMULATE_INTERVAL = 1


def test_animals():
    """Test a simulation of animals in the wild, each with different behaviour."""

    # Create lions and antelopes.
    animals = []
    for i in range(NUMBER_OF_LIONS):
        behaviour = CarnivoreBehaviour(chance_to_find_food=0.2, chance_to_catch_prey=0.5)
        animal = Animal("Lion", behaviour, gestation_period=3, starting_hunger=0.5)
        animals.append(animal)
    for i in range(NUMBER_OF_ANTELOPES):
        behaviour = HerbivoreBehaviour(chance_to_find_food=0.3)
        animal = Animal("Antelope", behaviour, starting_hunger=0.6)
        animals.append(animal)
    print(animals)

    # Simulate animals in the wild.
    days_simulated = 0
    while days_simulated < SIMULATE_MAX_DAYS:
        print("-" * 50 * len(animals))
        print(f"Simulation day {days_simulated}:")
        count_total = 0
        alive_total = 0
        for animal in animals:
            animal.simulate(SIMULATE_INTERVAL, animals)
            count_total += 1
            if animal.is_alive:
                alive_total += 1
        print(f"Total animals: {count_total}  Alive: {alive_total} {animals}")
        days_simulated += SIMULATE_INTERVAL


if __name__ == '__main__':
    test_animals()
