def quicksort(my_list):
    # recursion base case - empty list
    if not my_list:
        return []

    # first element is pivot
    pivot = my_list[0]

    # break up problem
    smaller = [x for x in my_list[1:] if x < pivot]
    greater = [x for x in my_list[1:] if x >= pivot]

    # recursively solve problem and recombine solutions
    return quicksort(smaller) + [pivot] + quicksort(greater)


print(quicksort([4, 4, 3, 2, 1, 8, 9]))
