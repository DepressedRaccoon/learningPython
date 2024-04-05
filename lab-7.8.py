
def displayNumberGrid():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    for i in range(rows):
        for j in range(1, columns + 1):
            print(j, end=" ")
        print()

def main():
    displayNumberGrid()
main()
