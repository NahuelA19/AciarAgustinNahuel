def order_insertion(list):
    for i in range(1, len(list)):
        word = list[i]
        j = i - 1
        while j >= 0 and len(word) < len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = word