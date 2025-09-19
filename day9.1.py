#Employee Salary Calculator with Overtime
class Employee:
  def __init__(self,Employee_Name,Working_Hours,Hourly_rate):
     self.Employee_Name= Employee_Name
     self.Working_Hours=Working_Hours
     self.Hourly_rate=Hourly_rate
  def  show_details(self,salary):
     print(f"Employee Name:{self.name}")
     print(f"Total Salary:₹{salary:.2f}")
#lambda for overtime calculation
overtime_pay=lambda extra_hours,rate:extra_hours*rate*1.5
def calculate_salary(rate,hours):
   if hours<40:
      return hours*rate
   else:
      regular=40*rate
      overtime=overtime_pay(hours-40,rate)
      return regular+overtime
name=input('Enter the Employee Name:').split()
rate=input('Enter the  Rate of Pay:').split()
hours=input('Enter No.of Working Hours:').split()
emp=Employee(name,rate,hours)
salary=calculate_salary(Hourly _rate, Hours_Worked)
   
   
    

 
 