from WorkersFabric import WorkerFactory
from MenuAbstractFabric import FactoryProducer as fp
from TablesPrototype import Tables


def divide():
    print(20 * '-')


w = WorkerFactory()
worker = w.hire_worker("Gordon Ramsay", experience=50, type_of_worker="chief")
print(worker)
print("Salary: " + str(worker.calculate_salary()))
new_worker = w.hire_worker("Jamie Oliver", 30, educated=False)
print(new_worker)
print("Salary: " + str(new_worker.calculate_salary()))
divide()

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
print(first_table, second_table, sep='\n')
print("First Table and Second Table are one object: " + str(id(first_table) == id(second_table)))
