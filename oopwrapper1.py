class employee():
    def __init__(self,name,p_id,age,salary):
        self.__id__=p_id
        self.name=name
        self.age=age
        self.__salary__= salary

    def __str__(self):
        return f"ID: {self.__id__}, Name: {self.name}, Age: {self.age}, Salary: {self.__salary__}"
    
    def display(self):
        print(f"ID: {self.__id__}, Name: {self.name}, Age:{self.age}, Salary: {self.__salary__}")

class manager(employee):
    def __init__(self, name, p_id, age, salary, dep):
        super().__init__(name, p_id, age, salary)
        self.department = dep

    def __str__(self):
        return super().__str__
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")
    
class developer(employee):
    def __init__(self, name, p_id, age, salary, prog_lang):
        super().__init__(name, p_id, age, salary)
        self.project = prog_lang
    
    def __str__(self):
            return super().__str__ 
    
    def display(self):
        super().display()
        print(f"Programing Language: {self.project}")
    
emp=[]

print("--- Employee Management System ---")
while True:
    print("Choose Operation")
    print("1. create a Employee")
    print("2. create a Manager")
    print("3. create a Developer")
    print("4. create a show details")
    print("5. create a compare salaries")
    print("6. create a Exit")

    choose=int(input("Choose your operation: "))

    if choose <=0 and choose >6:
        print("invalid choice")

    elif choose == 1:
        p_id=int(input("Enter your ID: "))
        name=input("Enter your name: ")
        age=int(input("Enter your Age: "))
        salary=float(input("Enter your Salary: "))

        print(f"Employee name: {name},Employee ID: {p_id}, Employee Age: {age}, Employee Salary: ₹{salary}")

        emp.append(employee(name,p_id,age,salary))

        print("Employee created successfully")

    elif choose == 2:
        p_id=int(input("Enter your ID: "))
        name=input("Enter your name: ")
        age=int(input("Enter your Age:"))
        salary=float(input("Enter your Salary: "))
        dep=input("Enter your Department: ")

        print(f"Manager Name: {name}, ID: {p_id}, Age: {age}, Salary: ₹{salary}, Department: {dep}")

        emp.append(manager(name, p_id, age, salary, dep))
        
        print("Manager created successfully")

    elif choose == 3:
        p_id=int(input("Enter your ID: "))
        name=input("Enter your name: ")
        age=int(input("Enter your Age:"))
        salary=float(input("Enter your Salary: "))
        prog_lang=input("Enter your Programing Language: ")

        print(f"Developer Name: {name}, ID: {p_id}, Age: {age}, Salary: ₹{salary}, Programing Language: {prog_lang}")

        emp.append(developer(name,p_id,age,salary,prog_lang))
        
        print("Manager created successfully")

    elif choose == 4:
       for i in emp:
           print(i)

    elif choose == 5:
        pass

    elif choose == 6:
        print("Exiting the program")
        break