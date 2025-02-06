month = 0
day = 0
year = 0 
if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
    print(f"{month}/{day}/{year}is a valid date.")
else:   
    print(f"{month}/{day}/{year}is an invalid day.")