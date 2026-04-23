def even_index_or_value(lt):
    result = []
    for i in range(len(lt)):
        if i % 2 == 0 or lt[i] % 2 == 0:
            result.append(lt[i])
    return result