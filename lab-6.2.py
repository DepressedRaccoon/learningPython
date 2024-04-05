def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    # Determine if num1 is the largest
    if num1 >= num2 and num1 >= num3:
        print ("The largest number is: ", num1)

    # Determine if num2 is the largest
    if num2 >= num1 and num2 >= num3:
        print ("The largest number is: ", num2)
    
    # Determine if num3 is the largest
    if num3 >= num1 and num3 >= num2:
        print ("The largest number is: ", num3)

main()