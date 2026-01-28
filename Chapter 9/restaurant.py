class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number_clients_served):
        self.number_served = number_clients_served

    def increment_number_served(self, increment):
        self.number_served += increment

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

    def display_clients(self):
        print(f"We had {self.number_served} clients today")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(flavor)


#restaurant = Restaurant("Ahmed Kebabs", "Turkish")
# osaka_foods = Restaurant("Osaka Foods", "Sata Andagi")
# brazilian_pizza = Restaurant("Cleyton Pizzaria", "Brazilian/Italian")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# osaka_foods.describe_restaurant()
# osaka_foods.open_restaurant()
# brazilian_pizza.describe_restaurant()
# brazilian_pizza.open_restaurant()

# restaurant.set_number_served(2)
# restaurant.display_clients()
# restaurant.increment_number_served(67)
# restaurant.display_clients()
#
# ahmed_icecream = IceCreamStand("Ahmed Ice Creams", "Turkish", "Pistachio", "Vanilla")
# ahmed_icecream.display_flavors()
