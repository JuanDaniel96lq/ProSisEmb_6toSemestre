class Student:
    full_name = ''
    last_name = ''

    def __init__(self, fn, ln):
    	self.full_name = fn
    	self.last_name = ln

    def get_full_name(self):
    	return self.full_name

    def set_last_name(self, ln):
    	self.last_name = ln

    def print_student(self):
    	print(self.full_name, self.last_name)
