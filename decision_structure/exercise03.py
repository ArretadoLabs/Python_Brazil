a = str(input())
first_letter = a[0].casefold()

if first_letter == 'm':
    print("male")
elif first_letter == 'f':
    print("female")
else:
    print("gender invalid")
