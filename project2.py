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
        print(f"Spell: {keyList[index]}")
        print("Spell Data:")
        for i in range(len(dataList[index])):
            print(f"{dataList[index][i]}")
    else:
        print("Invalid index value")

## Display all information 
def DisplayAllInformation(keyList, dataList): 
    print("All spells: ")
    print("Spell\t\tData")
    for i in range(len(keyList)):
        print(f"{keyList[i]}\t\t{dataList[i]}")

## Compare Two Items
def CompareTwoItems(keyList, dataList, index1, index2): 
    if index1 != -1 and index2 != -1:
        print(f"Comparing {keyList[index1]} and {keyList[index2]}:")
        print("1. Spell Data for Spell 1")
        print(dataList[index1])
        print("2. Spell Data for Spell 2")
        print(dataList[index2])
    else:
        print("Invalid index value for one or both spells")

## Ensure valid index 
def ValidateIndex(lst, index): 
    if index >= 0 and index < len(lst): 
        return True
    else: 
        return False

## Create menu function to display menu
def Menu(): 
    print("Menu:")
    print("1. Display information for a single spell")
    print("2. Display all information for each spell")
    print("3. Compare two spells")
    print("4. Exit")

## Create a main function / Basic template
def Main(): 

    ## List creation
    keyList = ["fireball", "bindingice", "fly", "antagonize", "powerwordkill", "soulcage", "primalsavagery", "sunbeam", "magehand", "spiritguardians", "spiritualweapon"]
    dataList = [["School: Evocation","Level: 3rd","Damage Type: Fire"], ["School: Evocation","Level: 2nd","Damage Type: Cold"], ["School: Transmutation","Level: 3rd","Damage Type: None"], ["School: Enchantment","Level: 3rd","Damage Type: Psychic"], ["School: Enchantment", "Level: 9th", "Damage Type: Yes"], ["School: Necromancy", "Level: 6th", "Damage Type: None"], ["School: Transmuatation", "Level: Cantrip", "Damage Type; Acid"], ["School: Evocation", "Level: 6th", "Damage Type: Radiant"], ["School: Evocation", "Level: Cantrip", "Damage Type: None"], ["School: Evocation", "Level: 3rd", "Damage Type: Radiant or Necrotic"], ["School: Evocation", "Level: 2nd", "Damage Type: Force"]]

    while True: 
        ## Call Rubric menu function
        Menu()
        choice = input("Enter your choice: ").lower().replace(" ", "")
        print(keyList)

        if choice == '1': 
            item = input("Enter the Spell to display: ").lower().replace(" ", "")
            index = FindItem(keyList, item)
            DisplayInformation(keyList, dataList, index)
        elif choice == '2': 
            DisplayAllInformation(keyList, dataList)
        elif choice == '3':
            item1 = input("Enter the first Spell: ").lower().replace(" ", "")
            item2 = input("Enter the second Spell: ").lower().replace(" ", "")
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