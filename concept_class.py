from datetime import datetime, date

# region Initial Scenario

# low reuse
# high duplicated code
# hard to maintain

client1 = {
    "name": "Lucio",
    "surname": "Fazio",
    "age": 29,
    "email": "lukfazio@gmail.com",
    "birth_date": "07/30/1994"
}

client2 = {
    "Name": "Maria",
    "Surname": "Fazio",
    "Age": 28,
    "Email": "example@example.com",
    "Birth_date": "07/29/1995"
}


def log_client1(client):
    print(client["surname"] + " , " + client["name"])


def log_client2(client):
    print(client["Surname"] + " , " + client["Name"])


# endregion

# region Applying Class and Objects
class Client:
    name: str
    surname: str
    age: int
    email: str
    birth_date: date

    def __init__(self, name_: str, surname_: str, age_: int, email_: str, birth_date_: date):
        self.name = name_
        self.surname = surname_
        self.age = age_
        self.email = email_
        self.birth_date = birth_date_

    def log_client(self):
        print(
            f"{self.surname}, {self.name}"
        )

    def _protected_method(self):
        print("That's a protected method, can be called by this class and heirs")

    def __private_method(self):
        print("That's a private method, can only be called by this class")


# Ensure the object are an instance of the class
new_client: Client = Client.__new__(Client)
new_client.name = "Lucio"
new_client.surname = "Fazio"
new_client.age = 29
new_client.email = "lukfazio@gmail.com"
new_client.birth_date = datetime.__new__(datetime, month=7, day=30, year=1994)
new_client.log_client()

# when you set a type in initialization of object, the PyCharm helps you warn about the wrong type
new_client = "test"

new_client2 = Client("Maria",
                     "Fazio",
                     28,
                     "exemple@exemple.com",
                     date(1995, 7, 29))
new_client2.log_client()

new_client2 = "test"

# endregion
