string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
symbol = '*'
for vowel in string:
    if vowel in vowels:
        string = string.replace(vowel, symbol)

print(string)
