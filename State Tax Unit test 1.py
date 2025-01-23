salary = 600000
num_dependents = 3  
state_tax=salary * 6.5 
federal_tax=salary * 28.0 
dependent_deduction=num_dependents * 2.5
total_withholding=state_tax + federal_tax + dependent_deduction   
take_home_pay=salary - total_withholding  
print("State Tax: $",round(state_tax,2))  
print("Federal Tax: $",round(federal_tax,2))  
print("Dependent Deducation: $",round(dependent_deduction,2))  
print("Salary:$",round(salary,2))   
print("Take-Home Pay: $",round(take_home_pay,2))    
     
  
