def filter_list(lst, a):
    new_lst = lst.copy()
    if a == 0:
        for number in lst:
            if number % 2 == 0:
                new_lst.remove(number)
        return new_lst
    else:
        for number in lst:
            if number % 2 == 1:
                new_lst.remove(number)
        return new_lst
print