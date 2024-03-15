

signMin = 35.00
numChars = int(input())
woodType = input()
color = input()
charge = float(signMin + ((numChars - 5) * 4))
if woodType == "oak":
    charge+=20.00
if color == "gold":
    charge+=15.00
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
