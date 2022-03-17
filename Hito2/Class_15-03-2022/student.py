class Student:
    full_name = ''
    last_name = ''

    def __init__(self):
        self.full_name = ""
        self.last_name = ""

    def get_full_name(self):
        return self.full_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, ln):
        self.last_name = ln

    def set_full_name(self, fn):
        self.full_name = fn

    def print_student(self):
        print(self.get_full_name(), self.get_last_name())