#
class Employee:
    def_init_(self,EmpName,EmpNum,Designation,Salary,DeptNo):
    self.EmpName=EmpName
    self.EmpNum=EmpNum
    self.Designation=EmpDesignation
    self.Salary=EmpSalary
    def display(self):
        print(f"Employee Name is :{self.EmpName}")
        print(f"Employee Num is:{self.EmpNum}")
        print(f"Employee Salary is:{self.EmpSalary}")
E1=Employee("Scott",20,"B.Tech",30000)
E1.display()
E2=Employee("Adams",21,"B.Tech",20000)
E2.display()
E3=Employee("Alice",25,"B.Tech",10000)
E3.display()


    