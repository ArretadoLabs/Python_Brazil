def unique_element_list(l):
    x = []
    for y in l:
        if y not in x:
            x.append(y)
    return x


print(unique_element_list([10, 20, 30, 10, 10, 20, 52]))
