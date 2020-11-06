# your code here
n = int(input())
sum = 0 
count = -1 
for i in 'a'*n:
    num = int(input())
    sum = sum + num
    count = count + 1
    if num == 0: 
        print(sum / count)
        break
