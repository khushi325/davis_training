# Program to calculate final price after discount
# This version validates input and uses a loop

while True:
    # Taking input from user
    price = float(input("Enter the price: "))
    discount = float(input("Enter discount percentage: "))
    
    # Validation: discount should not exceed 100%
    if discount <= 100:
        break
    else:
        print("Invalid discount! Please enter a value less than or equal to 100.")

# Calculating final price
final_price = price - (price * discount / 100)

# Displaying result
print("Final price after discount is:", final_price)