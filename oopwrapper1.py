class employee(): 
    def __init__(self, name, p_id, age, salary):
        self.__id__ = p_id
        self.name = name
        self.age = age
        self.__salary__ = salary

    def __str__(self):
        return f"ID: {self.__id__}, Name: {self.name}, Age: {self.age}, Salary: ₹{self.__salary__}"
    
    def display(self):
        print(f"ID: {self.__id__}, Name: {self.name}, Age:{self.age}, Salary: ₹{self.__salary__}")

    def __lt__(self, other):
        return self.__salary__ < other.__salary__

    def __gt__(self, other):
        return self.__salary__ > other.__salary__

    def __eq__(self, other):
        return self.__salary__ == other.__salary__

class manager(employee):
    def __init__(self, name, p_id, age, salary, dep):
        super().__init__(name, p_id, age, salary)
        self.department = dep

    def __str__(self):
        return super().__str__()

    def display(self):
        super().display()
        print(f"Department: {self.department}")
    
class developer(employee):
    def __init__(self, name, p_id, age, salary, prog_lang):
        super().__init__(name, p_id, age, salary)
        self.project = prog_lang
    
    def __str__(self):
        return super().__str__()

    def display(self):
        super().display()
        print(f"Programming Language: {self.project}")
    
emp={}

print("--- Employee Management System ---")
while True:
    print("Choose Operation:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Compare Salaries of Two Employees by ID")
    print("6. Exit")

    choose = int(input("Choose your operation: "))

    if choose <= 0 or choose > 6:
        print("Invalid choice, please select again.")

    elif choose == 1:
        p_id = int(input("Enter your ID: "))
        name = input("Enter your name: ")
        age = int(input("Enter your Age: "))
        salary = float(input("Enter your Salary: "))

        print(f"Employee name: {name}, Employee ID: {p_id}, Employee Age: {age}, Employee Salary: ₹{salary}")

        emp[p_id] = employee(name, p_id, age, salary)

        print("Employee created successfully.")

    elif choose == 2:
        p_id = int(input("Enter your ID: "))
        name = input("Enter your name: ")
        age = int(input("Enter your Age: "))
        salary = float(input("Enter your Salary: "))
        dep = input("Enter your Department: ")

        print(f"Manager Name: {name}, ID: {p_id}, Age: {age}, Salary: ₹{salary}, Department: {dep}")

        emp[p_id] = manager(name, p_id, age, salary, dep)
        
        print("Manager created successfully.")

    elif choose == 3:
        p_id = int(input("Enter your ID: "))
        name = input("Enter your name: ")
        age = int(input("Enter your Age: "))
        salary = float(input("Enter your Salary: "))
        prog_lang = input("Enter your Programming Language: ")

        print(f"Developer Name: {name}, ID: {p_id}, Age: {age}, Salary: ₹{salary}, Programming Language: {prog_lang}")

        emp[p_id] = developer(name, p_id, age, salary, prog_lang)
        
        print("Developer created successfully.")

    elif choose == 4:
        if not emp:
            print("No employees, managers, or developers created yet.")
        else:
            print("Employee Details:")
            for e in emp.values():
                e.display()

    elif choose == 5:
        emp1_id = int(input("Enter the first employee ID: "))
        emp2_id = int(input("Enter the second employee ID: "))
        
        if emp1_id not in emp or emp2_id not in emp:
            print("One or both employee IDs not found.")
        else:
            emp1 = emp[emp1_id]
            emp2 = emp[emp2_id]

            print(f"Comparing Employee {emp1.name} (ID: {emp1_id}) and Employee {emp2.name} (ID: {emp2_id}):")

            if emp1 > emp2:
                print(f"{emp1.name} has a higher salary than {emp2.name}")
            elif emp1 < emp2:
                print(f"{emp2.name} has a higher salary than {emp1.name}")
            else:
                print(f"{emp1.name} and {emp2.name} have equal salaries.")

    elif choose == 6:
        print("Exiting the program.")
        break
