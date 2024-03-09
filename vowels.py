# Write a program that counts the number of vowels in a sentence.


strings =  str(input("enter a statement :"))
vowels =set('aeiou')
found_vowels = set()
count = 0
for char in strings:
    if char in vowels:
        found_vowels.add(char.lower())
print(len(found_vowels))