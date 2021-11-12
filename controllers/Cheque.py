class Service:
    def request(self) -> str:
        return "Cheque is empty\n"


class Cheque:
    def __init__(self, order_id, table_id, waited_time, ordered_food, cost, waiter_name):
        self.order_id = order_id
        self.table_id = table_id
        self.waited_time = waited_time
        self.ordered_food = ordered_food
        self.cost = cost
        self.waiter_name = waiter_name

    def spec_request(self):
        return f"ID: {self.order_id}, ID_TABLE: {self.table_id}, TIME: {self.waited_time}, " \
               f"FOOD: {[item.name for item in self.ordered_food]}, COST: {self.cost}, WAITER: {self.waiter_name}"


class ParsedCheque(Service, Cheque):
    def request(self) -> str:
        order = self.spec_request()
        start = order.index("FOOD")
        return order[start:]


def client_request(target: "Service") -> str:
    return target.request()


if __name__ == "__main__":
    target = Service()
    print(client_request(target))

    cheque = Cheque(2, 2, 45, ["juice", "mamaliga"], 100, "Jane")
    cheque1 = ParsedCheque(1, 1, 30, ["pizza", "coffee"], 120, "Bryan")

    print("With adapter: " + client_request(cheque1))
    print("Without adapter: ", cheque.spec_request())
