def filter_list(royxat, son):
    for i in royxat:
        if son != 0:
            if i % 2 != 0:
                royxat.remove(i)
        else:
            if i % 2 == 0:
                royxat.remove(i)
    
    return royxat

print(filter_list([1, 2, 3, 4, 5, 6], 0))
