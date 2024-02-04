# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = 0.065 * salary
print("State Tax: $" + str(stateTax))
federalTax = 0.28 * salary
print("Federal Tax: $" + str(federalTax))
dependentDeduction = (salary * (numDependents * 0.025) ) 
#learned that python has a funny way of representing repeating decimals in float form so thats why I cast it a lot
#it had a 0.0000000000001 at the end cause the actual decimal value was repeating endlessly
print("Dependents: $" + str(float(int(dependentDeduction))))
totalWitholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
