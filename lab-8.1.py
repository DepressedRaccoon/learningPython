import math

def main():
    num = float(input("Enter a floating-point number: "))
    
    ceiling = math.ceil(num)
    floor = math.floor(num)
    
    if num <= 0:
        absoluteValue = abs(num)
        print("Ceiling:", ceiling)
        print("Floor:", floor)
        print("Absolute value:", absoluteValue)
    else:
        negation = -num
        squareRoot = round(math.sqrt(num), 3)
        print("Ceiling:", ceiling)
        print("Floor:", floor)
        print("Negation:", negation)
        print("Square root:", squareRoot)

main()
