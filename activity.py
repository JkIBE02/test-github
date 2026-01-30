#Car class
class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

    def display_info(self):
        print(f"Color: {self.color}, Model: {self.model}, Manufacturer: {self.manufacturer}")
        
# First 3 Car Objects
car1 = Car("Red", "Civic", "Honda")
car2 = Car("Blue", "Corolla", "Toyota")
car3 = Car("Black", "Model S", "Tesla")

# Display original properties
print("Original Car Properties:")
car1.display_info()
car2.display_info()
car3.display_info()

# Update car properties based on user input
def update_car(car, number):
    print(f"\nEnter new details for Car {number}:")
    car.color = input("Enter new color: ")
    car.model = input("Enter new model: ")
    car.manufacturer = input("Enter new manufacturer: ")

# Update car with user input
update_car(car1, 1)
update_car(car2, 2)

# Display updated properties
print("\nUpdated Car Properties:")
car1.display_info()
car2.display_info()
car3.display_info()
