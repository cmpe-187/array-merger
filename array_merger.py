__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"

""" Appends an index value to the merged list """
def add_to_list(list, index, new_list):
    new_list.append(list[index])
    index += 1

def array_merger(list1, list2):
    """ Variables to iterate through the lists """
    i = j = 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            add_to_list(list1, i, merged_list)
        else:
            add_to_list(list2, j, merged_list)

    """ Checks if there are any index values remaining in list1 and appends them """
    while i < len(list1):
        add_to_list(list1, i, merged_list)

    """ Has the same purpose as the previous while loop but for list2 instead """
    while j < len(list2):
        add_to_list(list2, j, merged_list)

    return merged_list
