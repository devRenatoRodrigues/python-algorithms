def quick_sort_strings(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [letter for letter in arr if letter < pivot]
    middle = [letter for letter in arr if letter == pivot]
    right = [letter for letter in arr if letter > pivot]

    return quick_sort_strings(left) + middle + quick_sort_strings(right)


def is_anagram(first_string, second_string):
    first_string = quick_sort_strings(first_string.lower())
    second_string = quick_sort_strings(second_string.lower())
    if len(first_string) == 0 or len(second_string) == 0:
        is_false = ("".join(first_string), "".join(second_string), False)
        return is_false
    for index in range(len(first_string)):
        if first_string[index] != second_string[index]:
            is_false = ("".join(first_string), "".join(second_string), False)
            return is_false
    else:
        is_true = ("".join(first_string), "".join(second_string), True)
        return is_true
