# import calcy

# result = calcy.add(10, 20)
# print(result)

# calcy.even_or_odd(51)

import employees

emp1 = employees.Employees('raju', 'sales', 'raju@gmail.com', 50000)
emp2 = employees.Employees('sabir', 'it', 'sabir@gmail.com', 60000)

emp1.emp_info()
emp2.emp_info()

emp1.change_department('devops')
emp1.emp_info()
