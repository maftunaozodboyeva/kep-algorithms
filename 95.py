def filter_list(royxat, son):
    natija = royxat.copy()
    
    for i in royxat:
        if son != 0:
            if i % 2 != 0:
                natija.remove(i)
        else:
            if i % 2 == 0:
                natija.remove(i)
    
    return natija

print(filter_list([1, 2, 3, 4, 5, 6], 0))














































# def filter_list(lst, n):
#     if n != 0:
#         return [x for x in lst if x % 2 == 0]
#     else:
#         return [x for x in lst if x % 2 != 0]
# print(filter_list([1, 2, 3, 4, 5, 6], 0))

#

