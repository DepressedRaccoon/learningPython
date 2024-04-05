def frameChoice():
    costs = []
    frame = input("Which Case Size would you like? Small, Medium, or Large? ").lower()
    while True: 
        if frame == "small": 
            cost = 120
            breakdown = "Case size: Small ($120)\n"
            costs.append((cost, breakdown))
            break
        elif frame == "medium": 
            cost = 210
            breakdown = "Case Size: Medium ($210)\n"
            costs.append((cost, breakdown))
            break
        elif frame == "large": 
            cost = 350
            breakdown = "Case Size: Large ($350)\n"
            costs.append((cost, breakdown))
            break
        else: 
            print("That is not a valid case size, try again!")
            frame = input("Which Case Size would like? Small, Medium, or Large? ").lower()
    return costs

def hardDriveChoice():
    costs = []
    hardDrive = input("Which Hard Drive would you like? Budget, Standard, or High End? ").lower()
    while True: 
        if hardDrive == "budget":
            cost = 100
            breakdown = "Hard Drive: Budget - 1TB HDD ($100)\n"
            costs.append((cost, breakdown))
            break
        elif hardDrive == "standard": 
            cost = 200
            breakdown = "Hard Drive: Standard - 1TB SSD ($200)\n"
            costs.append((cost, breakdown))
            break
        elif hardDrive == "high end": 
            cost = 350
            breakdown = "Hard Drive: High End - 5TB SSD ($350)\n"
            costs.append((cost, breakdown))
            break
        else: 
            print("That is not a valid Hard Drive option, try again!")
            hardDrive = input("Which Hard Drive would you like? Budget, Stardard, or High End? ").lower()
    return costs

def graphicsCardChoice():
    costs = []
    gCard = input("Which Graphics Card would you like? Budget, Standard, or High End? ").lower()
    while True: 
        if gCard == "budget":
            cost = 300
            breakdown = "Graphics Card: Budget - RTX 3060 ($300)\n"
            costs.append((cost, breakdown))
            break
        elif gCard == "standard": 
            cost = 690
            breakdown = "Graphics Card: Standard - RTX 4070ti  ($690)\n"
            costs.append((cost, breakdown))
            break
        elif gCard == "high end": 
            cost = 1820
            breakdown = "Graphics Card: High End - RTX 4090 ($1820)\n"
            costs.append((cost, breakdown))
            break
        else: 
            print("That is not a valid Graphics Card option, try again!")
            gCard = input("Which Graphics Card would you like? Budget, Standard, or High End? ").lower()
    return costs

def ramChoice():
    costs = []
    ram = input("How much RAM would you like? 8GB, 16GB, 32GB, 64GB, or 128GB? ").lower()
    while True: 
        if ram == "8gb":
            cost = 44
            breakdown = "RAM - 8GB ($44)\n"
            costs.append((cost, breakdown))
            break
        elif ram == "16gb": 
            cost = 60
            breakdown = "RAM - 16GB  ($60)\n"
            costs.append((cost, breakdown))
            break
        elif ram == "32gb": 
            cost = 100
            breakdown = "RAM - 32GB ($100)\n"
            costs.append((cost, breakdown))
            break
        elif ram == "64gb": 
            cost = 125
            breakdown = "RAM - 64GB ($125)\n"
            costs.append((cost, breakdown))
            break
        elif ram == "128gb": 
            cost = 400
            breakdown = "RAM - 128GB ($400)\n"
            costs.append((cost, breakdown))
            break
        else: 
            print("That is not a valid RAM option, try again!")
            ram = input("How much RAM would you like? 8GB, 16GB, 32GB, 64GB, or 128GB? (No spaces please!) ").lower()
    return costs

def calculateTotalCost(costs):
    totalCost = sum(cost for cost, _ in costs)
    breakdown = "\nTotal Cost Breakdown:\n"
    breakdown += '\n'.join(b for _, b in costs)
    return totalCost, breakdown

def buildDesktop():
    costs = []
    costs.extend(frameChoice())
    costs.extend(hardDriveChoice())
    costs.extend(graphicsCardChoice())
    costs.extend(ramChoice())

    totalCost, breakdown = calculateTotalCost(costs)

    print(breakdown)
    print("Total Cost: $" + str(totalCost))

def main():
    print("Welcome to Wayne's Computer Builder. Let's get started!")

    while True: 
        computerType = input("What type of computer would you like to build, a laptop or desktop? ").lower()

        if computerType == "desktop": 
            buildDesktop()
            break
        ## elif computerType == "laptop": 
            ## buildLaptop()
            break
        else: 
            print("I'm sorry, that is not a valid computer type, try again!")

main()
