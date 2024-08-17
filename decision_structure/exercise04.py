a = str(input())
letter = a[0].casefold()

if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
    print("consonant")
    print(letter)
else:
    print("vowel")
    print(letter)
