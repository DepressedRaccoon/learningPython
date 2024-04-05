def displayEvenNumbers():
    startValue = int(input("Enter a starting value: "))
    
    if startValue % 2 != 0:
        startValue -= 1

    if startValue < 2:
        return

    for i in range(startValue, 1, -2):
        print(i)

def main():
    displayEvenNumbers()

main() 
