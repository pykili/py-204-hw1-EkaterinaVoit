# your code here
string = input()
is_palindrom = False
a = ''
for i in string:
    a = i + a
if string == a:
    is_palindrom = True
print(is_palindrom)
