from typing import Any, List
def loopy_madness_with_while_loops(string1: str, string2: str) -> str:
    """
    The exact same function as loopy_madness from Lab 5, but we ask that you
    change any for loops that you used to while loops. Refer back to Lab 5 for
    the specifications of this function.
    """
    inter = ''
    if len(string1) <= len(string2):
        str3 = string1[::-1][1:]
        str4 = string1[1:]
        while len(string1) < len(string2) and len(string1) > 1:
            string1 += str3 + str4
        string1 = string1 * len(string2)
        i=0
        while i<len(string2):
            inter += string1[i] + string2[i]
            i+=1
    elif len(string1) > len(string2):
        str3 = string2[::-1][1:]
        str4 = string2[1:]
        while len(string2) < len(string1) and len(string2) > 1:
            string2 += str3 + str4
        string2 = string2 * len(string1)
        i=0
        while i<len(string1):
            inter += string1[i] + string2[i]
            i+=1
    return inter
def longest_chain(lst: List[int]) -> int:
    i=0
    length = 0
    while i<len(lst):
        if lst[i] == 1:
            length +=1
        elif lst[i] == 0:
            return length
        i+=1
    return length
def count_types(lst: List[Any]) -> List[int]:
    i = 0
    lst1 = []
    lst2 = []
    while i < len(lst):
        if (type(lst[i])) not in lst2:
            lst2.append(type(lst[i]))
            lst1.append(1)
        else:
            lst1[lst2.index(type(lst[i]))] += 1
        i += 1
    return lst1
def second_largest(lst: List[int]) -> int:
    i = 1
    while len(lst) - 1 >= i:
        j = len(lst) - 1
        while j >= i:
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
        i += 1
    return lst[-2]
