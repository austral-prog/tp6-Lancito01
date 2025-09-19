# Replace the "ANSWER HERE" with your answer


def remove_elements(list_to_remove_elements):
    # remove first, fifth, and sixth element
    if len(list_to_remove_elements) == 0:
        return list_to_remove_elements
    del list_to_remove_elements[0]
    del list_to_remove_elements[3:6]
    return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    return list_to_check == []


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    return list_to_compare1[2] == list_to_compare2[2]


def list_of_lists(list_of_lists_to_modify):
    [list1, list2, list3] = list_of_lists_to_modify
    list1 = list1[:2]
    list2 = list2[1:4]
    list3 = list3[-2:]
    return [list1, list2, list3]
