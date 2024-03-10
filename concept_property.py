class ImplementProperty:
    def __init__(self, public_: str, private_: str):
        self.public_attribute = public_
        self.__private_attribute = private_

    @property
    def private_attribute(self):
        return self.__private_attribute

    @private_attribute.setter
    def private_attribute(self, value_):
        self.__private_attribute = value_

# To test, use the Python Console:
# from concept_property import ImplementProperty
# obj = ImplementProperty("public", "private")
# obj.public_attribute
# >> 'public'
# obj.__private_attribute
# AttributeError: 'ImplementProperty' object has no attribute '__private_attribute'
