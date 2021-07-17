# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Director import Director
from Employee import Employee
from Manager import Manager


def try_polymorphism():
    # Use a breakpoint in the code line below to debug your script.
    employee_raise()
    manager_raise()
    director_raise()


def get_emp_salaries(emp_list):
    for emp in emp_list:
        print(emp.salary, " "+ str(emp.emp_id))


def test_bulk_raise():
    emp1 = Employee(1001, 50000)
    emp2 = Manager(1002, 100000)
    emp3 = Director(1003, 200000)

    emp_list = [emp1, emp2, emp3]
    bulk_raise(emp_list)
    get_emp_salaries(emp_list)


def bulk_raise(list_of_emp):
    for emp in list_of_emp:
        emp.give_raise()


# Press the green button in the gutter to run the script.
def director_raise():
    director = Director(1002, 100000)
    director.give_raise()
    print("director salary after hike" + str(director.salary))


def manager_raise():
    mgr = Manager(1002, 100000)
    mgr.give_raise()
    print("mgr salary after hike" + str(mgr.salary))


def employee_raise():
    emp1 = Employee(1001, 56000)
    print(emp1.salary, " " + str(emp1.emp_id))
    emp1.give_raise()
    print('salary after raise' + str(emp1.salary))


if __name__ == '__main__':
    # try_polymorphism()
    test_bulk_raise()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
