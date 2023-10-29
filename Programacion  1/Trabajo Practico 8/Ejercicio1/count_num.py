def count_num(n):

    if n<10:
        return 1
    else:
        return 1 + count_num(n//10)
