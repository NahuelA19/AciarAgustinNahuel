def combo(list, k, current='', result=[]):
    if k == 0:
        result.append(current)
    else:
        for caracter in list:
            combo(list, k - 1, current + caracter, result)
    return result



