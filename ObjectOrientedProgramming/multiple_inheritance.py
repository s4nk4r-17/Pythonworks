#Multiple Inheritance

class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def display_person_info(self):

        print(self.name,self.age) 


class Employee:

    def __init__(self,emp_id,salary):

        self.emp_id=emp_id
        self.salary=salary

    def display_employee_info(self):

        print(self.emp_id,self.salary)

class Manager(Person,Employee):

    def __init__(self, name,age,emp_id,salary,department):

        self.department=department

        Person.__init__(self,name,age)

        Employee.__init__(self,emp_id,salary)
        
    def display_manager_info(self):

        self.display_person_info()

        self.display_employee_info()

        print(self.department)


manager_instance=Manager("ram",22,102,32000,"hr")

manager_instance.display_manager_info()


#________________________________________________

class Cusine:

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

class MealType:

    def __init__(self,name):

        self.name=name

class Dish(Cusine,MealType):

    def __init__(self, cusine_name,name,dish_name):

        Cusine.__init__(self,cusine_name)

        MealType.__init__(self,name)

        self.dish_name=dish_name

    def display_dish_info(self):

        print("Cusine :",self.cusine_name)
        print("Meal Type :",self.name)
        print("Dish Name :",self.dish_name)


dish_instance=Dish("Italian","Dinner","Lasagna")

dish_instance.display_dish_info()
