# Program to print even numbers between 1 and N
# This version uses a different logic than the previous one

# Taking input from the user
N = int(input("Enter the value of N: "))

print("Even numbers between 1 and", N, "are:")

# Starting loop directly from 2 and increasing by 2
for i in range(2, N + 1, 2):
    print(i, end=" ")