def main():
    print("Begin program")
    
    names = []
    name = input("Enter a name: ")

    while name != "STOP":
        names.append(name)
        name = input("Enter a name: ")

    # Display all the names entered
    for name in names:
        print(name)

main()