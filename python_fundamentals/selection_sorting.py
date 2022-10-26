
# def function_name(arguments1, arguments2):
#     return arguments1 + arguments2
#
# print(function_name(2, 4))


# Write a function to sort a list of integers in ascending order
ints = [7, 5, 2, 912, 1999, 1]
def sort(ints):
    # Selection Sort --
    # (1)Loop through the list to find the element that is the smallest.
    # (2)Swapping the smallest element with the element at the start
    # (3)Repeat steps (1) and (2) on the remaining elements
    i = 0
    while(i < len(ints)):
        #(1)
        second_half_of_list = ints[i:]   # everything after i
        smallest_seen = min(second_half_of_list)
        smallest_index = i + second_half_of_list.index(smallest_seen)  # gets index to ints our original list

        #(2)
        ints[smallest_index] = ints[i]                  # Puts front of list where smallest number is
        ints[i] = smallest_seen                         # Put smallest number in front of list
        i = i + 1
    return ints

print(sort(ints))

