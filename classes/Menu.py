from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class Caprese(Product):
    name = "Caprese Salad with Pesto Sauce"

    def cook(self):
        print("Italian appetizer prepared: " + self.name)


class Lasagna(Product):
    name = "Lasagne with Bechamel Sauce"

    def cook(self):
        print("Italian main course prepared: " + self.name)


class Tiramisu(Product):
    name = "Tiramisu with Panna Cotta"

    def cook(self):
        print("Italian dessert prepared: " + self.name)


class Sarmale(Product):
    name = "Sarmale"

    def cook(self):
        print("Moldavian appetizer prepared: " + self.name)


class Polenta(Product):
    name = "Mamaliga cu Branza si Smantana"

    def cook(self):
        print("Moldavian main course prepared: " + self.name)


class CrepesCake(Product):
    name = "Cusma lui Guguta"

    def cook(self):
        print("Moldavian dessert prepared: " + self.name)


class Factory(ABC):
    @abstractmethod
    def get_dish(type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "appetizer":
            return Caprese()
        if type_of_meal == "main":
            return Lasagna()
        if type_of_meal == "dessert":
            return Tiramisu()


class MoldavianDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "appetizer":
            return Sarmale()
        if type_of_meal == "main":
            return Polenta()
        if type_of_meal == "dessert":
            return CrepesCake()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "moldavian":
            return MoldavianDishesFactory
        if type_of_factory == "italian":
            return ItalianDishesFactory


if __name__ == "__main__":
    factory = FactoryProducer()
    chosen_factory = factory.get_factory("moldavian")
    order_main = chosen_factory.get_dish("main")
    order_main.cook()

    order_dessert = chosen_factory.get_dish("dessert")
    order_dessert.cook()

    order_appetizer = chosen_factory.get_dish("appetizer")
    order_appetizer.cook()

    print("-" * 20)

    chosen_factory = factory.get_factory("italian")
    order_main = chosen_factory.get_dish("main")
    order_main.cook()

    order_appetizer = chosen_factory.get_dish("appetizer")
    order_appetizer.cook()

    order_dessert = chosen_factory.get_dish("dessert")
    order_dessert.cook()
