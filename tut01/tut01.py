def factorial(x):
    product = 1
    for i in range(1,x+1):
        product = product*i
    print("The factorial of " + str(x) + " is " + str(product))
    

x=int(input("Enter the number whose factorial is to be found"))
factorial(x)
