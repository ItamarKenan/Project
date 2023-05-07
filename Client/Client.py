import requests
from Employee import Employee

isOpen = True

def testServer():
    print(requests.get(url='/test').text)
    pass
def addEmployee(name,id):
    employee= Employee(name,id)

def getEmployeeById(id):
    pass

def getEmployeeByName(name):
    pass

def getAllEmployees():
    pass

def updateEmployee(name,id):
    pass

def deleteEmployee(name):
    pass

def importEmployeesFromCsv():
    pass


def exportEmployeesToCsv():
    pass


functions = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeById,
    3: getEmployeeByName,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee,
    7: importEmployeesFromCsv,
    8: exportEmployeesToCsv,
    9: exit
}



def printMenu():
    print("0. Test Server")
    print("1. Add employee")
    print("2. Get employee by ID")
    print("3. Get employee by name")
    print("4. Get all employees")
    print("5. Update employee")
    print("6. Delete employee")
    print("7. Import employees from file")
    print("8. Export employees to file")
    print("9. Exit")


    pass

def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())
        testServer()

if __name__ == "__main__":
    main()