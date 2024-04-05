# Write a program that will prompt the user to enter the lengths of three line segments and
# determine if they can form a valid triangle.

def main():
    side1 = float(input("Enter the first segment: "))
    side2 = float(input("Enter the second segment: "))
    side3 = float(input("Enter the third segment: "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("These segments can form a valid triangle.")
    else:
        print("These segments cannot form a valid triangle.")

main()
