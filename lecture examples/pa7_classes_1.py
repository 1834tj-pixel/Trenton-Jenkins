class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __repr__(self):
        return f"Vehicle(brand={self.brand}, speed={self.speed})"

    def __str__(self):
        return f"A {self.brand} vehicle that goes {self.speed} mph"

    def accelerate(self, amount):
        self.speed += amount
        return self.speed

    def describe(self):
        return f"This vehicle is made by {self.brand}."


class Car(Vehicle):
    def __init__(self, brand, speed, doors, mpg):
        super().__init__(brand, speed)
        self.doors = doors
        self.mpg = mpg

    def __repr__(self):
        return f"Car(brand={self.brand}, speed={self.speed}, doors={self.doors}, mpg={self.mpg})"

    def __str__(self):
        return f"A {self.brand} car with {self.doors} doors that gets {self.mpg} mpg"

    def car_feature(self):
        return f"This car has {self.doors} doors."

    def parent_speed_info(self):
        return f"The parent speed is {self.speed} mph."


class Truck(Vehicle):
    def __init__(self, brand, speed, towing_capacity, bed_length):
        super().__init__(brand, speed)
        self.towing_capacity = towing_capacity
        self.bed_length = bed_length

    def __repr__(self):
        return f"Truck(brand={self.brand}, speed={self.speed}, towing={self.towing_capacity}, bed={self.bed_length})"

    def __str__(self):
        return f"A {self.brand} truck with {self.towing_capacity} lb towing capacity"

    def truck_feature(self):
        return f"This truck can tow {self.towing_capacity} pounds."

    def parent_brand_info(self):
        return f"The parent brand is {self.brand}."


class Motorcycle(Vehicle):
    def __init__(self, brand, speed, cc, style):
        super().__init__(brand, speed)
        self.cc = cc
        self.style = style

    def __repr__(self):
        return f"Motorcycle(brand={self.brand}, speed={self.speed}, cc={self.cc}, style={self.style})"

    def __str__(self):
        return f"A {self.cc}cc {self.style} motorcycle by {self.brand}"

    def moto_feature(self):
        return f"This motorcycle engine is {self.cc}cc."

    def parent_speed_check(self):
        return f"Parent speed value: {self.speed}"
