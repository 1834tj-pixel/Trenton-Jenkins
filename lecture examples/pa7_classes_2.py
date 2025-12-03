class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def __repr__(self):
        return f"Animal(species={self.species}, age={self.age})"

    def __str__(self):
        return f"A {self.age}-year-old {self.species}"

    def speak(self, sound):
        return f"The {self.species} says '{sound}'!"

    def describe(self):
        return f"This animal is a {self.species}."


class Dog(Animal):
    def __init__(self, species, age, breed, weight):
        super().__init__(species, age)
        self.breed = breed
        self.weight = weight

    def __repr__(self):
        return f"Dog(species={self.species}, age={self.age}, breed={self.breed}, weight={self.weight})"

    def __str__(self):
        return f"A {self.age}-year-old {self.breed} dog weighing {self.weight} lbs"

    def dog_feature(self):
        return f"This dog is a {self.breed}."

    def parent_age_info(self):
        return f"Parent age is {self.age}."


class Cat(Animal):
    def __init__(self, species, age, color, claws_sharpness):
        super().__init__(species, age)
        self.color = color
        self.claws_sharpness = claws_sharpness

    def __repr__(self):
        return f"Cat(species={self.species}, age={self.age}, color={self.color}, sharpness={self.claws_sharpness})"

    def __str__(self):
        return f"A {self.color} cat who is {self.age} years old"

    def cat_feature(self):
        return f"This cat has {self.claws_sharpness} sharpness claws."

    def parent_species_info(self):
        return f"Parent species: {self.species}."


class Bird(Animal):
    def __init__(self, species, age, wingspan, can_fly):
        super().__init__(species, age)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def __repr__(self):
        return f"Bird(species={self.species}, age={self.age}, wingspan={self.wingspan}, can_fly={self.can_fly})"

    def __str__(self):
        return f"A {self.age}-year-old bird with {self.wingspan} ft wingspan"

    def bird_feature(self):
        return f"This bird's wingspan is {self.wingspan} feet."

    def parent_description(self):
        return f"Parent species: {self.species}."
