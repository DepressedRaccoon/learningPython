def main():
    operand1 = float(input("Enter a number: "))
    operator = input("Enter an operator: ")
    operand2 = float(input("Enter a number: "))
    # STEP 1: If the user entered an operator other than
    # *, /, + or - then display an error message and terminate
    # with exit().

    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("ERROR: Invalid operator")
        exit()


    # STEP 2: Determine if the operator entered was / (division)
    # and the 2nd operand was zero. If so, display an error
    # message and terminate with exit().
        
    if operator == '/' and operand2 == 0:
        print("ERROR: Cannot divide by zero")
        exit()

    # STEP 3: Calculate and store the answer into the
    # variable result.
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2

    print()
    print("The result:", result)

main()
