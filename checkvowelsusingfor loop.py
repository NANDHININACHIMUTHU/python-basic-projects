ch=input("Enter the Character").lower()
vowels="aeiou"
is_vowel=False

for v in vowels:
    if len(ch)==1 and ch==v:
        is_vowel=True
        break
if is_vowel:
    print("vowels")
else:
    print("Conatants")
                