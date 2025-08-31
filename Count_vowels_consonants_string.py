def Count_vowels_consonants_string(string):
    vowel = 0
    consonant = 0
    for i in string:
        if i.isalpha():
            i=i.lower()
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'I' or i == 'O' or i == 'U' or i == 'E' :
                vowel+1
            else:
                consonant+=1
    return vowel,consonant

string=input("Enter string: ")
result=Count_vowels_consonants_string(string)
print("Vowel Count in the String : ",result[0])
print("Consonant Count in the String : ",result[1])