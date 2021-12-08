from abc import ABC, abstractmethod
from random import randrange
from typing import List

states = {1: "Closed", 2: "Opened", 3: "Event", 4: "Free Food", 5: "Repair"}


class IRestaurantJournal(ABC):

    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    def notify(self):
        pass


class RestaurantJournal(IRestaurantJournal):
    _state = None
    _subscribers = []

    def subscribe(self, subscriber):
        print("One new subscriber!")
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        print("One unsubscriber!:(")
        self._subscribers.remove(subscriber)

    def notify(self):
        print("Notifying subs...")
        for sub in self._subscribers:
            pass

    def change_state(self):
        self._state = randrange(1, 6)
        print(f"Restaurant now is in state {states[self._state]}")
        self.notify()


class Subscriber(ABC):
    @abstractmethod
    def update(self, journal):
        pass


class WantsToVisit(Subscriber):
    def update(self, journal):
        if journal._state >= 2 and journal._state != 5:
            print("Updated for lovers!")


class Other(Subscriber):
    def update(self, journal):
        if journal._state == 1 or journal._state == 5:
            print("Updated for others!")


if __name__ == "__main__":
    journal = RestaurantJournal()
    sub1 = WantsToVisit()
    journal.subscribe(sub1)

    sub2 = Other()
    journal.subscribe(sub2)

    journal.change_state()
    journal.change_state()

    journal.unsubscribe(sub2)

    journal.change_state()

