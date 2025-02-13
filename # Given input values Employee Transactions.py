# Given input values
employee_name = "employee name"
num_shifts = 0
num_transactions = 0
transaction_dollar_value = 0

# Calculate productivity score
if num_transactions > 0 and num_shifts > 0:  # Avoid division by zero
    productivity_score = (transaction_dollar_value / num_transactions) / num_shifts
else:
    productivity_score = 0  # Default to zero if invalid inputs

# Determine the bonus using nested if statements
if productivity_score <= 30:
    bonus = 50.00
else:
    if productivity_score <= 69:
        bonus = 75.00
    else:
        if productivity_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

# Output results
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.2f}")  # Ensure two decimal formatting
