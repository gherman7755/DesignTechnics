from abc import ABC, abstractmethod


class General(ABC):
    @abstractmethod
    def request(self):
        pass


class DataBase(General):
    def __init__(self, cookers):
        self.cookers = cookers

    def request(self):
        for cooker in self.cookers:
            print(cooker)


class Check(General):
    def __init__(self, db: DataBase, login, password):
        self._db = db
        self.login = login
        self.password = password

    def request(self):
        if self.check_access(self.login, self.password):
            self._db.request()

    def check_access(self, login: str, password: str):
        if login == "admin" and password == "admin":
            return True
        else:
            print("Incorrect Login or Password")


def client_access(general: General):
    general.request()


if __name__ == "__main__":
    db = DataBase(["Jimmy", "Nate"])
    client_access(db)

    check = Check(db, "admin", "1123435")
    client_access(check)

