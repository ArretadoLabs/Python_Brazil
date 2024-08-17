list_empty = []
list_pair = []
list_odd = []

for x in range(0, 10):
    a = int(input())
    if a % 2 == 0:
        list_pair.append(a)
    else:
        list_odd.append(a)

print("pair list: ", list_pair)
print("odd list: ", list_odd)
