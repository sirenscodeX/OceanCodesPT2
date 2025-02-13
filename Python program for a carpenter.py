# Define variables
charge = 0.00
numChars = 18
color = "black"
woodtype = "oak"

# Base charge for all signs
charge = 35.00

# Additional character cost (first 5 are included)
if numChars > 5:
    charge += (numChars - 5) * 4.00  # $4 per additional character

# Extra charge for oak wood
if woodtype == "oak":
    charge += 20.00

# Extra charge for gold-leaf lettering
if color == "gold":
    charge += 15.00

# Display final price
print(f"The charge for this sign is ${charge:.2f}.")
    