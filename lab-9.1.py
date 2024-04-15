## Given the already declared array shoppingList, display the elements with index 3, 6, 9, 2, 4, 6 in that order.

def main():
## Starter Array
    shoppingList = ["eggs", "milk", "sausage", "bread", "apple juice", "Snickers", "carrots", "sliced turkey", "ketchup", "cheese"]

    list = [3, 6, 9, 2, 4, 6]

    for index in list: 
        print(f"{index}: {shoppingList[index]}")

main() 
