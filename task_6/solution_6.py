# your code here
a = int(input())
stairs = str(a) * a
b = 1
for i in stairs:
    print(str(a) * b)
    b = b + 1
