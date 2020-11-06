alphabet = ''
a = ''
for smth in 'a'*10:
    user_input = input()
    a = user_input + a
for i in a:
    if i not in alphabet:
        alphabet = alphabet + i
print(alphabet)
