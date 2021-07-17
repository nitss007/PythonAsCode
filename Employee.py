class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def give_raise(self):
        self.salary = self.salary * 1.05
