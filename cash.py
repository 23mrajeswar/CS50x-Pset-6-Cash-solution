from cs50 import get_float

# Prompt the user for change
change = get_float("Change owed: ")

# If the change owed is a negative number, re-prompt the user for change
while change < 0:
    change = get_float("Change owed: ")
    
# Changing change in dollars to cents
cents = round(100 * change)

# Initialize number of coins variable
coins = 0

# Deducting Quarters
while cents >= 25:
    cents = cents - 25
    coins += 1
    
# Deducting Dime
while cents >= 10:
    cents = cents - 10
    coins += 1
    
# Deducting Nickels
while cents >= 5:
    cents = cents - 5
    coins += 1

# Deducting Pennies
while cents >= 1:
    cents = cents - 1
    coins += 1

# Print the number of coins required
if cents == 0:
    print(coins, end="")

print()