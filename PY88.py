#7. Create an Employee class that stores an employee's name, basic salary, house rent allowance (HRA) percentage, travel allowance, and deductions. 
# Add instance methods to calculate gross salary and net salary. Gross salary is the basic salary plus HRA and travel allowance.
# Net salary is gross salary minus deductions. Display the employee's name, gross salary, and net salary


class Employee:
    def __init__(self, name, basic, hra_percent, travel, deductions):
        self.name = name
        self.basic = basic
        self.hra_percent = hra_percent
        self.travel = travel
        self.deductions = deductions

    def gross_salary(self):
        hra = self.basic * self.hra_percent / 100
        gross = self.basic + hra + self.travel
        return gross

    def net_salary(self):
        net = self.gross_salary() - self.deductions
        return net

    def display(self):
        print("Employee Name:", self.name)
        print("Gross Salary:", self.gross_salary())
        print("Net Salary:", self.net_salary())


name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
hra_percent = float(input("Enter HRA percentage: "))
travel = float(input("Enter travel allowance: "))
deductions = float(input("Enter deductions: "))

emp = Employee(name, basic, hra_percent, travel, deductions)
emp.display()
