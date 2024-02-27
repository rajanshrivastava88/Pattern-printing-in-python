# Number Pattern in Python


n = int(input("Enter the Number of Rows : "))
num = 1

for i in range(1, n+1):
    for col in range(1, i+1):
        print(num, end=" ")
        num=num+1
    print()

# Star Pattern

n = int(input("Enter the Number  of Rows : "))

for rows in range(1, n+1):
    for cols in range(1, rows+1):
        print("*", end = "  ")
    print()
