# Program to print even numbers between 1 and N

# Taking input from user
N = int(input("Enter the value of N: "))

# Loop from 1 to N
for i in range(1, N + 1):
    
    # Check if number is even
    if i % 2 == 0:
        print(i, end=" ")