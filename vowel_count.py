def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lower_string = string.lower()
    count_vowel = 0

    for i in lower_string:
        for vowel in vowels:
            if i == vowel:
                count_vowel += 1
    return count_vowel


sen = input("Please enter a sentence: ")
print(vowel_count(sen))
