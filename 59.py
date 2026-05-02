# Algorith
# 1. max_1 ni topish
# sonlarni ichidan max_1 o'chiramiz
# 3. qolgan sonlar ichidan max topish

def max_2(*args):
    max_1 = max(args)
    lst = list(args)
    lst.remove(max_1)
    return max(lst)
print(max_2(1, 2, 3, 4, 5))
    
# def max_2(*args):
#     sorted_args = sorted(args)
#     return sorted_args[-2]
