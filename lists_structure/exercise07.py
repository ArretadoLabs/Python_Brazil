"""
Smaller number in list
"""


def smaller_number_list(list_number):
    smaller_number = list_number[0]

    for x in list_number:
        if x < smaller_number:
            smaller_number = x

    return smaller_number


# Calling function
print(smaller_number_list([10, 2, 5, -8]))
