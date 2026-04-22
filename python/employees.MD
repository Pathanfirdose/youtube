Good choice starting with classes—this is a solid beginner example. I’ll walk you through it step by step in a simple way so you understand what’s happening.

First, this line defines a class:

```python
class Employees:
```

A **class** is like a blueprint or template. It tells Python how to create employee objects.

Inside the class, this line:

```python
COMPANY = 'white money PVT LTD'
```

is a **class variable**. It belongs to the class itself, not to individual employees. So every employee will share the same company name.

Next:

```python
def __init__(self, name, department, email, salary):
```

This is a **constructor** (special method). It runs automatically when you create an object.

* `self` means “this current object”
* The rest (`name`, `department`, etc.) are inputs you pass while creating an employee.

These lines:

```python
self.name = name
self.department = department
self.email = email
self.salary = salary
```

store the values inside the object. So each employee will have their own name, department, etc.

Now this method:

```python
def emp_info(self):
```

This is a function inside the class (called a **method**). It prints employee details using the stored values:

```python
print(f'Name is {self.name}')
```

Here `self.name` means “get the name of this specific employee”.

Next method:

```python
def change_department(self, new_dapart):
```

This updates the department:

```python
self.department = new_dapart
```

So if you call this method, the employee’s department changes.

Now object creation:

```python
emp1 = Employees('raju', 'sales', 'raju@gmail.com', '50000')
emp2 = Employees('sabir', 'it', 'sabir@gmail.com', '60000')
```

Here you are creating two employees:

* `emp1` → raju
* `emp2` → sabir

Each gets its own data.

Then:

```python
emp1.emp_info()
emp2.emp_info()
```

This calls the method and prints details of each employee.

Next:

```python
emp1.change_department('devops')
```

This changes **only emp1’s department** to devops.

Then:

```python
emp1.emp_info()
```

Now it will show updated department for emp1.

Finally:

```python
print(emp1.COMPANY)
print(emp2.COMPANY)
```

Both print the same value because `COMPANY` is shared (class variable).

---

**Simple summary:**

* Class = blueprint
* Object (emp1, emp2) = real employees
* `self` = current object
* `__init__` = runs when object is created
* Methods = actions (like print info, change department)
* Class variable = shared by all objects

---

One small improvement: your salary is stored as a string `'50000'`. It’s better to store it as a number:

```python
50000
```

If you want, I can show you how to add features like salary increment or employee ID next.
