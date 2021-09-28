# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:20:14 2021

@author: APARNA
"""

class Employee:
    hike = 1.04
    
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay  =  pay 
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@gmail.com"
        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay*self.hike
        
class Developer(Employee):
    hike = 2.04
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []
    
    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        print(len(self.employees))
        for emp in self.employees:
            print("-->",emp.fullname())
        
dev1 = Developer("Aparna", "Mane",1000000,["Python","C++"])
dev2 = Developer("Vinayak","Magokar",1500000,["Python","C++","ML"])

mgr1 = Manager("Jetin","Mathew",25000000,[dev1])

print(mgr1.email)
mgr1.add_employees(dev2)
mgr1.remove_employees(dev1)
mgr1.print_employees()

print(isinstance(mgr1,Manager)) #true
print(isinstance(mgr1,Employee)) #true
print(isinstance(dev1,Manager))#false
print(isinstance(dev2,Developer)) #true

print(issubclass(Developer,Employee)) #true
print(issubclass(Developer,Manager)) #false
print(issubclass(Manager,Employee))#true
print(e1.email)
print(e1.prog_lang)

print(e2.fullname())
print(e2.employees)


e1.apply_raise()
print(e1.pay)
