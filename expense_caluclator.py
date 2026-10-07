print("PERSONAL EXPENSE CALCULATOR")
print("---------------------------")

income = float(input("Enter your monthly income: ₹"))

food = float(input("Enter food expenses: ₹"))
travel = float(input("Enter travel expenses: ₹"))
education = float(input("Enter education expenses: ₹"))
shopping = float(input("Enter shopping expenses: ₹"))
other = float(input("Enter other expenses: ₹"))

total_expenses = food + travel + education + shopping + other
savings = income - total_expenses

print("\n----- EXPENSE SUMMARY -----")
print("Income: ₹", income)
print("Food: ₹", food)
print("Travel: ₹", travel)
print("Education: ₹", education)
print("Shopping: ₹", shopping)
print("Other: ₹", other)

print("Total Expenses: ₹", total_expenses)
print("Savings: ₹", savings)

if savings > 0:
    print("Status: You have savings.")
elif savings == 0:
    print("Status: No savings.")
else:
    print("Status: You are spending more than your income.")