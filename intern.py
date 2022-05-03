from internship import Internship
from people import People

class Intern(People, Internship):
    def __init__(self, name: str, identity_document: str):
        People.__init__(self, name, identity_document)
        Internship.__init__(self)