nameList = []
wageList = []
hourList = []

#input name
name = input("Enter the name of the employee.  ")

while name != "end":
    nameList.append(name.upper())

    #input wage
    wage = float(input("Enter the wage.  "))
    wageList.append(wage)

    #input hours
    hour = float(input("Enter the hours worked.  "))
    hourList.append(hour)

    name = input("Enter the name of the employee.  ")
    
for x in range(len(nameList)):
    print (nameList[x])
    salary = wageList[x] * hourList[x]
    print (salary)
