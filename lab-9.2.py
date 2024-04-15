def main():
    print("Begin program")
    # the rest of your code goes below
    shoppingList = ["eggs", "milk", "sausage", "bread", "apple juice", "Snickers", "carrots", "sliced turkey", "ketchup", "cheese"]

    for i, item in enumerate(shoppingList, start=1):
        print(f"{i}, {item}")

main()