from Employee import Employee


class Director(Employee):
    def give_raise(self):
        self.salary = self.salary * 1.20