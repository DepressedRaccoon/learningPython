def frameChoice():
    costs = []
    while True:
        frame = input("Which Case Size would you like? Small, Medium, or Large? ").lower()
        if frame == "small":
            cost = 120
            breakdown = "Case size: Small ($120)\n"
            costs = [(cost, breakdown)]
            break
        elif frame == "medium":
            cost = 210
            breakdown = "Case Size: Medium ($210)\n"
            costs = [(cost, breakdown)]
            break
        elif frame == "large":
            cost = 350
            breakdown = "Case Size: Large ($350)\n"
            costs = [(cost, breakdown)]
            break
        else:
            print("That is not a valid case size, try again!")
    return costs

def hardDriveChoice():
    costs = []
    while True:
        hardDrive = input("Which Hard Drive would you like? Budget, Standard, or High End? ").lower()
        if hardDrive == "budget":
            cost = 100
            breakdown = "Hard Drive: Budget - 1TB HDD ($100)\n"
            costs = [(cost, breakdown)]
            break
        elif hardDrive == "standard":
            cost = 200
            breakdown = "Hard Drive: Standard - 1TB SSD ($200)\n"
            costs = [(cost, breakdown)]
            break
        elif hardDrive == "high end":
            cost = 350
            breakdown = "Hard Drive: High End - 5TB SSD ($350)\n"
            costs = [(cost, breakdown)]
            break
        else:
            print("That is not a valid Hard Drive option, try again!")
    return costs

def graphicsCardChoice():
    costs = []
    while True:
        gCard = input("Which Graphics Card would you like? Budget, Standard, or High End? ").lower()
        if gCard == "budget":
            cost = 300
            breakdown = "Graphics Card: Budget - RTX 3060 ($300)\n"
            costs = [(cost, breakdown)]
            break
        elif gCard == "standard":
            cost = 690
            breakdown = "Graphics Card: Standard - RTX 4070ti  ($690)\n"
            costs = [(cost, breakdown)]
            break
        elif gCard == "high end":
            cost = 1820
            breakdown = "Graphics Card: High End - RTX 4090 ($1820)\n"
            costs = [(cost, breakdown)]
            break
        else:
            print("That is not a valid Graphics Card option, try again!")
    return costs

def ramChoice():
    costs = []
    while True:
        ram = input("How much RAM would you like? 8GB, 16GB, 32GB, 64GB, or 128GB? ").lower()
        if ram == "8gb":
            cost = 44
            breakdown = "RAM - 8GB ($44)\n"
            costs = [(cost, breakdown)]
            break
        elif ram == "16gb":
            cost = 60
            breakdown = "RAM - 16GB  ($60)\n"
            costs = [(cost, breakdown)]
            break
        elif ram == "32gb":
            cost = 100
            breakdown = "RAM - 32GB ($100)\n"
            costs = [(cost, breakdown)]
            break
        elif ram == "64gb":
            cost = 125
            breakdown = "RAM - 64GB ($125)\n"
            costs = [(cost, breakdown)]
            break
        elif ram == "128gb":
            cost = 400
            breakdown = "RAM - 128GB ($400)\n"
            costs = [(cost, breakdown)]
            break
        else:
            print("That is not a valid RAM option, try again!")
    return costs

def calculateTotalCost(costs):
    totalCost = sum(cost for cost, _ in costs)
    breakdown = "\nTotal Cost Breakdown:\n"
    breakdown += '\n'.join(b for _, b in costs)
    return totalCost, breakdown

def buildDesktop():
    costs = []
    costs += frameChoice()
    costs += hardDriveChoice()
    costs += graphicsCardChoice()
    costs += ramChoice()

    totalCost, breakdown = calculateTotalCost(costs)

    print(breakdown)
    print("Total Cost: $" + str(totalCost))

def main():
    print("Welcome to Wayne's Computer Builder. Let's get started!")

    while True:
        computerType = input("Did you want to build a desktop? Yes/no? ").lower()

        if computerType == "yes":
            buildDesktop()
            break
        elif computerType == "no":
            print("My apologies, run this program again when ready!")
            break
        else:
            print("I'm sorry, that is not a valid computer type, try again!")

main()