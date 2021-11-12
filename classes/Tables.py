from abc import ABC


class Prototype(ABC):
    def clone(self):
        pass


class Tables(Prototype):
    def __init__(self, number, cost):
        self.number = number
        self.cost = cost

    def clone(self):
        new_table = Tables(self.number, self.cost)
        return new_table

    def __str__(self):
        return "Table Number: " + str(self.number) + " Cost: " + str(self.cost)


if __name__ == "__main__":
    first_table = Tables(1, 120)
    print(first_table)
    second_table = first_table.clone()
    print(second_table)
    print("First and Second Tables are one object: " + str(id(first_table) == id(second_table)))