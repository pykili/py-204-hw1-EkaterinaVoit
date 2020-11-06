# your code here
numbers = input('введите последовательность цифр: ')
a = 0
for number in numbers:
    if int(number) > a:
        a = int(number)
print(a)
