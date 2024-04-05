def calculateGradeAverage():
    total = 0
    count = 0

    while True:
        grade = float(input("Enter grade: "))
        if grade < 0:
            break
        total += grade
        count += 1

    if count > 0:
        average = total / count
        print(f"Grade average: {average}")
    else:
        print("No grades entered.")


def main():
    calculateGradeAverage()


main()
