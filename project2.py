## Welcome to Project 2! This is the first commit! 



## Create menu function to display menu
def Menu(): 
    print("Menu:")
    print("1. Display information for a single item")
    print("2. Display all information for each item")
    print("3. Compare two items")
    print("4. Exit")

## Create a main function / Basic template
def Main(): 

    ## List creation
    keyList = ["Something", "Something1", "Something2", "Something3", "Something4", "Something5"]
    dataList = [[1,2,3], [3,5,6], [7,8,9], [10,11,12], [13,14,15]]

    while True: 
        ## Call Rubric menu function
        Menu()
        choice = input("Enter your choice: ")

        if choice == '1': 
            item = input("Enter the item to display: ")
            index = FindItem(keyList, item)
            DisplayInformation(keyLIst, dataLIst, index)
        elif choice == '2': 
            DisplayAllInformation(keyList, dataList)
        elif choice == '3':
            item1 = input("Enter the first item: ")
            item2 = input("Enter the second item: ")
            index1 = FindItem(keyList, item1)
            index2 = FindItem(keyList, item2)
            CompareTwoItems(keyList, dataList, index1, index2)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice")

## Call Main
    Main()