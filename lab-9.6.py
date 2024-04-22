def main(): 
    def findProduct(products, choice): 
        if choice in products:
            return products.index(choice)
        else: 
            return -1 
    
    def displayProductInformation(products, prices, index): 
        if index != -1: 
            print("Product:", products[index])
            print("Price:", prices[index])
        else: 
            print("Can't find product.")

    print("Begin program")

    products = ["eggs", "milk", "sausage", "bread", "apple"]
    prices = [2.99, 4.99, 5.99, 3.49, 1.22]

    choice = input("Enter a product: ").lower()

    while choice != "STOP": 
     index = findProduct(products, choice)
     displayProductInformation(products, prices, index)
     choice = input("Enter a product: ")

main()