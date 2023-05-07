class Employee:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setAge(self, age):
        self.age = age

    def __json__(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
        }