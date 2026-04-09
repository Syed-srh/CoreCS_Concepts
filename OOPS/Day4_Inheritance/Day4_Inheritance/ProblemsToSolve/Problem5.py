# 5: Multi-Talent System (Multiple Inheritance)
# Complete the Musician, Athlete, and Person classes.

# Musician class:
# Add below methods:
# play_instrument() : Prints instrument playing message
# Athlete class:
# Add below methods:
# play_sport() : Prints sport playing message
# Person class:
# The Person class inherits from both Musician and Athlete.

# Features to be added to Person class
# Add below attributes:
# name
# Add below methods:
# show_talents() : Calls both parent methods

class Musician:
    def __init__(self, instrument):
        self.instrument = instrument
    
    def playing_instrument(self):
        print(f"Playing the {self.instrument}")

class Athelete:
    def __init__(self, sport):
        self.sport = sport
    
    def playing_sport(self):
        print(f"Playing {self.sport}")

class Person(Musician, Athelete):
    def __init__(self, name, instrument, sport):
        self.name = name
        Musician.__init__(self, instrument)
        Athelete.__init__(self, sport)
    
# Example usage:
person = Person("John", "Guitar", "Football")
person.playing_instrument()
person.playing_sport()

