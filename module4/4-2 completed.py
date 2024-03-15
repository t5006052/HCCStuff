name = input()
shifts = int(input())
transactions = int(input())
transvalue = float(input())
valuePerTrans = float(transvalue/transactions)
productivity = float(valuePerTrans/shifts)
bonus = 0.0
if productivity >= 200:
    bonus = 200.00
elif productivity >= 70:
    bonus = 100.00
elif productivity >= 30:
    bonus = 75.00
else:
    bonus = 50.00
print("Employee Name: " + name)
print("Employee Bonus: $" + str(bonus))

