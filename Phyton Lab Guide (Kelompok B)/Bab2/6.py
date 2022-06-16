class Employee:  
    'Base class of all employees'   
    empCount = 0
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
         print("Name : ", self.name, ", Salary: ", self.salary)
# Create the first object of the Employee class.     
emp1 = Employee("Zara", 2000)    
# Create the second object of the Employee class.     
emp2 = Employee("Manni", 5000)     
emp1.displayEmployee()   
emp2.displayEmployee()    
print("Total Employee %d" % Employee.empCount)    