from functools import total_ordering, reduce, partial

class Employee:
    def __init__(self, name):
        self.name = name

# Create a list of employees
employees = [Employee("Dave"),Employee("Ava"),Employee("Joe"),Employee("Mark")]

def email(id, domain, extension):
    return f"{id}@{domain}.{extension}"

dzone_email = partial(email, domain='dzone', extension='com')

print(dzone_email.index(1))

print(dzone_email('support'))
for emp in employees:
    print(dzone_email(emp.name.lower()))



'''--- Partial (Email Generation) ---
 Partial allows you to 'freeze' some arguments of a function (domain and extension),
 creating a new, simpler function (dzone_email) that only needs the remaining arguments.
'''