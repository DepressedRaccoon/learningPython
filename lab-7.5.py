# Use this replit to develop your code
# Complete the function displaySquares()

def displaySquares():
    num = int(input("Enter an integer: "))
    for i in range(1, num + 1):
        print(i * i)

def main():
    displaySquares()

main()