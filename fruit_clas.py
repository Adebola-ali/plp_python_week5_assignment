# Base Class
class Fruit:
    def __init__(self, name, color, taste, weight):
        self.name = name
        self.color = color
        self.taste = taste
        self.weight = weight 

    def description(self):
        return f"The {self.name} is {self.color} and tastes {self.taste}."

    def is_healthy(self):
        return True  

    def get_weight_in_kg(self):
        return self.weight / 1000


# Derived Class: Citrus Fruit
class Citrus(Fruit):
    def __init__(self, name, color, taste, weight, vitamin_c_content):
        super().__init__(name, color, taste, weight)
        self.vitamin_c_content = vitamin_c_content  # mg per 100g

    # Polymorphism: Overriding the description method
    def description(self):
        return (
            f"The {self.name} is a citrus fruit, {self.color} in color, "
            f"tastes {self.taste}, and is rich in Vitamin C ({self.vitamin_c_content} mg/100g)."
        )


# Testing the classes
# Create a generic fruit
apple = Fruit("Apple", "red", "sweet", 200)
print(apple.description())
print(f"Weight in kg: {apple.get_weight_in_kg()} kg")
print(f"Is it healthy? {apple.is_healthy()}")

# Create a citrus fruit
orange = Citrus("Orange", "orange", "tangy", 150, 53)
print(orange.description())
print(f"Weight in kg: {orange.get_weight_in_kg()} kg")
print(f"Is it healthy? {orange.is_healthy()}")
