def main():
    print("Begin program")
    # the rest of your code goes below
    productPrices = [10.99, 13.74, 3.29, 5.69, 100.0, 89.99, 19.35, 14.25]

    total = sum(productPrices)

    average = total/len(productPrices)

    averageRounded = round(average, 2)

    print("Average product price:", averageRounded)

main()