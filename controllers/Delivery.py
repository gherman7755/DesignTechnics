from __future__ import annotations


class OnlineOrder:
    def __init__(self, kitchen: Kitchen, transport: Transport) -> None:
        self._kitchen = kitchen or Kitchen()
        self._transport = transport or Transport()

    def make_order(self, food: list, address):
        self._kitchen.prepare_food(food)
        self._kitchen.send_cheque()
        self._transport.take_food()
        self._transport.find_transport(address)


class Kitchen:
    def prepare_food(self, food: list):
        print("Order is ready")

    def send_cheque(self):
        print("Order cost created")


class Transport:
    def take_food(self) -> str:
        print("Food is take from kitchen")

    def find_transport(self, address):
        print(f"Transport is available... Go to: {address}")


def client_order(online: OnlineOrder, food, address):
    online.make_order(food, address)


if __name__ == "__main__":
    transport = Transport()
    kitchen = Kitchen()
    online = OnlineOrder(kitchen, transport)
    client_order(online, ["pizza", "juice"], "Baker Street, 221b")

