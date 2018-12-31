import sqlite3

class Employees:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property    
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
          {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  Where first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees Where 
                  first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employees('John', 'Doe', 80000)
emp_2 = Employees('Jane', 'Doe', 90000)

# =============================================================================
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (
#         emp_1.first, emp_1.last, emp_1.pay))
# 
# conn.commit()
# 
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# 
# conn.commit()
# 
# c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
# 
# print(c.fetchall())
# 
# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
# 
# print(c.fetchall())
# 
# conn.commit()
# =============================================================================

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
conn.close()
