from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Chief(Product):
    def __init__(self, name: str, work_experience: int):
        self.name = name
        self.experience = work_experience
        self.base_salary = 800

    def calculate_salary(self) -> int:
        return round((self.experience + self.base_salary) * 1.5)

    def __str__(self):
        return "Chief - " + self.name + " -" * 5 + " Experience: " + str(self.experience)


class Cooker(Product):
    def __init__(self, name: str, age: int, educated: bool):
        self.name = name
        self.age = age
        self.educated = educated
        self.base_salary = 400

    def calculate_salary(self) -> int:
        if self.educated:
            return round(self.base_salary * 1.5)
        else:
            return self.base_salary

    def __str__(self):
        if self.educated:
            return "Worker - " + self.name + " -" * 5 + " Age: " + str(self.age) + " \tEducated"
        else:
            return "Intern - " + self.name + " -" * 5 + " Age: " + str(self.age) + " \tStudent"


class WorkerFactory:
    def hire_worker(self, name, age=None, experience=None, educated=None, type_of_worker="intern"):
        if type_of_worker == "chief":
            return Chief(name, experience)
        if type_of_worker == "intern":
            return Cooker(name, age, educated)


if __name__ == "__main__":
    factory = WorkerFactory()
    product = factory.hire_worker("Jack", experience=30, type_of_worker="chief")
    print(product)

    product2 = factory.hire_worker("Jimmy", 30, educated=False)
    print(product2)

    product3 = factory.hire_worker("Ramsay", 18, educated=True)
    print(product3)
