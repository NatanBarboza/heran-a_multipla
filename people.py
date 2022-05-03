from abc import ABC


class People(ABC):
    def __init__(self, name:str, identity_document:str):
        self.__name = name
        self.__identity_document = identity_document

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def identity_document(self):
        return self.__identity_document

    @identity_document.setter
    def identity_document(self, new_value):
        self.__identity_document = new_value

    def validate_identity(self):
        return True