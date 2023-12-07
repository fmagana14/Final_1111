class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink
     
    def my_order(self):
        order_instance = Order(self, self.favorite_drink)
        return order_instance.to_string()
    

class Order:
    def __init__(self, person, drink_type):
        self.person = person
        self.drink_type = drink_type

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}"


class Barista(Person):
    def __init__(self, name, greeting):
        super().__init__(name, favorite_drink="")
        self.greeting = greeting
    
        

    
class CoffeeBar:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self.barista = None

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        for order in self.orders_list:
            if self.barista:
                print(self.barista.greeting)
            print(order.person.name, "orders:", order.drink_type)

# Create instances of Person
amy_instance = Person("Amy", "Coffee")
bob_instance = Person("Bob", "Tea")
cat_instance = Person("Cat", "Milk")

kevin_barista = Barista("Kevin", "Hey dude!")

my_coffee_bar = CoffeeBar("CafeDelNando")
# Call my_order method on each Person instance
order1 = Order(amy_instance, amy_instance.favorite_drink)
order2 = Order(bob_instance, bob_instance.favorite_drink)
order3 = Order(cat_instance, cat_instance.favorite_drink)

kevin_order = kevin_barista.my_order()

my_coffee_bar.place_order(order1)
my_coffee_bar.place_order(order2)
my_coffee_bar.place_order(order3)
my_coffee_bar.barista = kevin_barista
# Print order strings
my_coffee_bar.process_orders()

# stuck on challenge 10 don't know how
