
# TASK 4: Loops & Iterations

# For loop: print numbers 1–100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")  # print in single line
print("\n")  # new line

# While loop: countdown timer from 10
print("Countdown from 10:")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Lift-off!\n")

# Break and continue example
print("Numbers 1–10, skipping 5 and stopping at 8:")
for i in range(1, 11):
    if i == 5:
        continue  # skip number 5
    if i == 8:
        break     # stop loop at number 8
    print(i, end=" ")
print("\n")

# Iterate over string characters
message = "Python"
print("Characters in 'Python':")
for char in message:
    print(char, end=" ")
print("\n")

# Multiplication table of 7
print("Multiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")
print()

# Range with steps
print("Even numbers from 2 to 20 using range with steps:")
for i in range(2, 21, 2):  # start=2, stop=21, step=2
    print(i, end=" ")
print("\n")

# Combine loop with conditions: print all multiples of 3 from 1–50
print("Multiples of 3 from 1 to 50:")
for i in range(1, 51):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")

# Real-world example: simple shopping cart
print("Shopping cart total for 5 items:")
prices = [150, 200, 50, 75, 100]
total = 0
for price in prices:
    total += price
print("Total amount:", total)
