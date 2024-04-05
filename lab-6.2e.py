# Write a program that will prompt the user for 3 numbers, then display the largest of the 3. Write it using if-else statements. 

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

# FINISH ME
    
    if num1 >= num2 and num1 >= num3: 
        print ("The largest number is: ", num1)
    
    elif num2 >= num1 and num2 >= num3: 
        print("The largest number is: ", num2)
    
    elif num3 >= num1 and num3 >+ num2: 
        print("The largest number is: ", num3)
main()