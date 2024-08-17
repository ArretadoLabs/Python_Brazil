list_empty = []
list_consonant = []

for x in range(0,10):
    a = str(input())
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        list_consonant.append(a)

size_list_consonant = len(list_consonant)

print(list_consonant)
print(size_list_consonant)