a = int(input("Enter the number"))
m = 0
if a % 2 == 0:
    m = a - 1
else:
    m = a
n = 1
for i in range(1, m + 1):
    print(n, end=" ")
    n += 2
