## Welcome to Project 2! This is the first commit! 

## Create Function to find idex of items
def FindItem(lst, item):
    try: 
        index = lst.index(item)
        return index
    except ValueError:
        return -1

## Display information for single item
def DisplayInformation(keyList, dataList, index):
    if index != -1: 
        print(f"Item: {keyList[index]}")
        print("Data:")
        for i in range(len(dataList[index])):
            print(f"{dataList[index][i]}")
    else:
        print("Invalid index value")

## Display all information 
def DisplayAllInformation(keyList, dataList): 
    print("All info: ")
    print("Item\t\tData")
    for i in range(len(keyList)):
        print(f"{keyList[i]}\t\t{dataList[i]}")


## Ensure valid index 
def ValidateIndex(lst, index): 
    if index >=9 and index < len(lst): 
        return True
    else: 
        return False

## Compare Two Items
def CompareTwoItems(keyList, dataList, index1, index2): 
    if index1 != -1 and index2 != -1:
        print(f"Comparing {keyList[index1]} and {keyList[index2]}:")
        print("1. Data for item 1")
        print(dataList[index1])
        print("2. Data for item 2")
        print(dataList[index2])
    else:
        print("Invalid index value for one or both items")

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
            DisplayInformation(keyList, dataList, index)
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