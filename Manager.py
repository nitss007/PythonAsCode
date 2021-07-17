from Employee import Employee


class Manager(Employee):
    def give_raise(self):
        self.salary = self.salary * 1.10