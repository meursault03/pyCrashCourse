import restaurant

restaurant_instance = restaurant.Restaurant("Rose Pizzas", "Italian")
restaurant_instance.describe_restaurant()
restaurant_instance.open_restaurant()
restaurant_instance.set_number_served(67)
restaurant_instance.display_clients()
restaurant_instance.increment_number_served(33)
restaurant_instance.display_clients()

icecream_instance = restaurant.IceCreamStand("Rose Ice Creams", "Desserts", "Chocolate", "Strawberry", "Mango")
icecream_instance.describe_restaurant()
icecream_instance.open_restaurant()
icecream_instance.display_flavors()