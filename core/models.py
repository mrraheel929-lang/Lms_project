from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self._email = email  # Encapsulation

    @abstractmethod
    def get_role(self):
        pass

class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.courses = []

    def get_role(self):
        return "Student"

class Teacher(User):
    def __init__(self, user_id, name, email, department):
        super().__init__(user_id, name, email)
        self.department = department

    def get_role(self):
        return "Teacher"
