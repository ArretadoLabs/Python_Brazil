"""
Biggest number
"""


def bigger_number_list(list_number):
    big_number = list_number[0]
    for x in list_number:
        if x > big_number:
            big_number = x
    return big_number


# Calling function
print(bigger_number_list([10, 2, 3, 4, 5]))
