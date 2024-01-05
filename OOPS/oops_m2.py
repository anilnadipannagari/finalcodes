class Employee:
    Department='Employee'
    Principal='Naidu'
    Adviser='Raja kumar'
    def insert(obj,name,age,salary,idn):
        obj.name=name
        obj.age=age
        obj.salary=salary
        obj.id=idn
anil=Employee()
pavan=Employee()
Employee.insert(anil,'kumar',23,30900,5)
Employee.insert(pavan,'kumar',23,30900,5)
d=anil.name
print(d)
anil.insert('gaanafa reddy',23,40000,'tes076')