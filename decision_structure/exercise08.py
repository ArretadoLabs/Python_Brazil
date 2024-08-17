shift = str(input())
shift_lower = shift[0].casefold()

if shift_lower == 'm':
    print("matutino")
elif shift_lower == 'v':
    print("verspertino")
elif shift_lower == 'n':
    print("noturno")
else:
    print("invalid")
