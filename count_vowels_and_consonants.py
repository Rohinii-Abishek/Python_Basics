def count_vowels_and_consonants(s):
    vowels="aeiouAEIOU"
    new_vowels=0
    new_consonants=0
    for char in s:
        if char.isalpha():
            if char in vowels:
                new_vowels+=1
            else:
                new_consonants+=1
    return new_vowels,new_consonants
user_input=input("Enter the string:")
result=count_vowels_and_consonants(user_input)
print(f"The number of vowels and consonants in the word{user_input} are {result} respectively")                