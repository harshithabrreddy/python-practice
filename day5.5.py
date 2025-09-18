#
string=input('Enter the string:').lower()
vowel,consonant=0,0
for ch in string:
    if ch.isalpha():
        vowel+=1
    else:
        consonant+=1
    print(f"vowel count is{vowel}")
    print(f"consonant count is{consonant}")