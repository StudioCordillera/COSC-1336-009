def main():
    #creating lists
    nameList = []
    wageList = []
    hourList = []

    #input name
    name = input("Enter the name of the employee.  ")
    while name != "ugly":
        nameList.append(name.upper())

        #input wage
        wage = float(input("Enter the wage.  "))
        wageList.append(wage)
      

        #input hours
        hour = float(input("Enter the hours worked.  "))
        hourList.append(hour)
       
        name = input("Enter the name of the employee.  ")


    payRoll = calcPay(nameList, wageList, hourList)
    print("The total payroll is ",payRoll)

#calculates pay        
def calcPay(nameList, wageList, hourList):
    
    payList = []
    totalPayRoll = 0
    
    for i in range (len(nameList)):
        pay = wageList[i] * hourList[i]
        payList.append(pay)
        totalPayRoll = totalPayRoll + pay 
        print(nameList[i], " is paid ",payList[i])
        
    return totalPayRoll

    
main()
