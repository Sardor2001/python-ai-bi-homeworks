string = input("Enter a string: ")

vowels = 'aeiouAeiou'

vowel_count = sum(1 for char in string if char.isalpha() and char in vowels)
consonant_count = sum(1 for char in string if char.isalpha() and char not in vowels)

print(f"vowels: {vowel_count}, consonants: {consonant_count}")
