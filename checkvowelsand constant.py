ch=input("Enter the character").lower()

if len(ch)==1 and ch.isalpha():
    if ch in 'aeiou':
        print("vowels")
    else:
        print("Constant")
else:
    print("Not alpha")
