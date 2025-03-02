txt = input("Enter a string: ")

vowels = 'aeiouAEIOU'

mySet = set(vowels)
result = []
j = 0
for i in range(0, len(txt)):
    result.append(txt[i])
    j += 1
    if (j >= 3) and not (txt[i] in mySet) and i != len(txt) - 1:
        result.append('_')
        mySet.add(txt[i])
        j = 0

print(''.join(str(x) for x in result))
