# Write a program that will prompt the user for a number and display "Positive" if the number is
#greater than zero, "Negative" if it is less than zero, or "Zero" if it is zero.

# Prompting the user 
number = float(input("Enter a number: "))

# Check if the number is positive
if number > 0:
    print("Positive")

# Checkif the number is negative
if number < 0:
    print("Negative")

# Check if the number is zero
if number == 0:
    print("Zero")
