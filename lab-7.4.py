def validateAge():
    min_age = int(input("Enter minimum age: "))
    max_age = int(input("Enter maximum age: "))

    while True:
        age = int(input("Enter your age: "))
        if min_age <= age <= max_age:
            break
        else:
            print("Sorry, invalid age entered.")

def main():
    validateAge()

main()
