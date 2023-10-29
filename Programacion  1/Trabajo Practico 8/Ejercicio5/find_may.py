def find_may(list):
    if not list:
        return None
    
    if len(list)==1:
        return list[0]
    
    first_element= list[0]
    may_en_restante= find_may(list[1:])

    return first_element if first_element> may_en_restante else may_en_restante