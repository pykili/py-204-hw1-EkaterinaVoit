# your code here
string = input()
count1 = 0
count2 = 0
b = string[0]
c = string[0]
occured_twice = False
for i in string:
    d = b + i
    count2 = 0
    count1 += 1
    for a in string:
        e = c + a
        count2 += 1
        if d == e and count1 != count2 and count1 != 1 and count2 != 1:
            occured_twice = True
        c = a
    b = i
print(occured_twice)
