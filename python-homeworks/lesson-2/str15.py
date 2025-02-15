sentence = input("Enter a sentence: ")
acronym_list = [word[0].capitalize() for word in sentence.split()]
acronym = ''
for character in acronym_list:
    acronym = acronym+character
print(acronym)

