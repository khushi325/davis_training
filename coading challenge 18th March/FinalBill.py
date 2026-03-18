# Program to calculate the final bill after discount

# Taking input for price
price = float(input("Enter the price of the product: "))

# Taking input for discount percentage
discount = input("Enter the discount percentage: ")

# Removing % symbol if the user enters it
discount = discount.replace("%", "")

# Converting to float
discount = float(discount)

# Calculating discount amount
discount_amount = (price * discount) / 100

# Calculating final price
final_price = price - discount_amount

# Display result
print("Final price after discount is:", final_price)