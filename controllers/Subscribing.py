import random

from classes.Workers import WorkerFactory
from classes.Menu import FactoryProducer as fp
from classes.Tables import Tables
from controllers.DataBase import DataBase, Check
from controllers.Cheque import ParsedCheque, client_request
from controllers.Delivery import Kitchen, Transport, OnlineOrder, client_order
from controllers.Subscribing import RestaurantJournal, WantsToVisit, Other


def divide():
    print(20 * '-')


w = WorkerFactory()
worker = w.hire_worker("Gordon Ramsay", experience=50, type_of_worker="chief")
new_worker = w.hire_worker("Jamie Oliver", 30, educated=False)

# Proxy. Checks if someone can access it
db = DataBase([worker, new_worker])
check = Check(db, "admin", "admin")


factory = fp()
italian_kitchen = factory.get_factory("italian")
main_order = italian_kitchen.get_dish("main")
main_order.cook()

moldavian_kitchen = factory.get_factory("moldavian")
dessert_order = moldavian_kitchen.get_dish("dessert")
dessert_order.cook()

divide()

first_table = Tables(1, 1500)
second_table = first_table.clone()

# Adapter
cheque = ParsedCheque(1, first_table.number, 25, [main_order, dessert_order], first_table.cost, "Jane")
print("First table ordered: ", client_request(cheque))

main_order = moldavian_kitchen.get_dish("main")
dessert_order = italian_kitchen.get_dish("dessert")

# Facade
transport = Transport()
kitchen = Kitchen()
order = OnlineOrder(kitchen, transport)
client_order(order, [main_order, dessert_order], "Baker Street 221b")

divide()

# Observer
journal = RestaurantJournal()
number_subscribers = random.randint(1, 10)
subs = []
for i in range(number_subscribers):
    sub = random.choice([WantsToVisit(), Other()])
    subs.append(sub)
    journal.subscribe(sub)

journal.change_state()
journal.change_state()


# print(first_table, second_table, sep='\n')
# print("First Table and Second Table are one object: " + str(id(first_table) == id(second_table)))
