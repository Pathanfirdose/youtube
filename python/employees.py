class Employees:
    COMPANY = 'white money PVT LTD' 

    def __init__(self, name, department, email, salary):
        self.name = name
        self.department = department
        self.email = email
        self.salary = salary

    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'Department is {self.department}')
        print(f'mail is {self.email}')
        print(f'salary is {self.salary}')

    def change_department(self, new_dapart):
        self.department = new_dapart
        print(f'new dapartment is {new_dapart}')
        





