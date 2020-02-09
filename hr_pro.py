class Employee:
    def __init__ (self,name,age,salary,employment_year):
       self.name = name
       self.age = int(age)
       self.salary = int(salary)
       self.employment_year = int(employment_year)
    def get_working_years(self):
        wy = 2020 - self.employment_year
        return wy




class Manager(Employee):
    def __init__ (self,name,age,salary,employment_year,bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = float(bonus_percentage)
    def get_bonus(self):
        bonus = self.bonus_percentage * self.salary
        return bonus







def main():
	# main code here

    n = 0
    employees_list = []
    managers_list = []

    while n != 5 :
        print ("""
            Welcome to HR Pro 2019
        Options:
            1. Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
            """
        )
        n = int(input("What would you like to do?"))

        if n == 1 :
            for x in employees_list:
                print (f"name : {x.name}")
                print (f"age :{str(x.age)}")
                print (f"salary : {str(x.salary)}")
                print (f"working years : {x.get_working_years()}")
                print()
                continue
        elif n == 2 :
            for x in managers_list:
                print (f"name : {x.name} ")
                print (f"age :{str(x.age)}")
                print (f"salary : {str(x.salary)}")
                print (f"working years : {x.get_working_years()}")
                print (f"bonus : {x.get_bonus()}")
                continue
        elif n == 3 :
            na = input("name: ")
            ag = int(input("age: "))
            sl = int(input("slary: "))
            ey = int(input("employment year : "))
            per = Employee(na,ag,sl,ey)
            employees_list.append(per)
            print("Employee added succesfully")
        elif n==4 :
            na = input("name: ")
            ag = int(input("age: "))
            sl = int(input("slary: "))
            ey = int(input("employment year : "))
            bp = float(input("Bonus Percentage: "))
            per = Manager(na,ag,sl,ey,bp)
            managers_list.append(per)
            print("Manager added succesfully")
        else :
            continue








if __name__ == '__main__':
	main()
