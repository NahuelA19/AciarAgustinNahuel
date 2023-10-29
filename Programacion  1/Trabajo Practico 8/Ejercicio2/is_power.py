def is_power(num,base):
    if num ==1:
        return True
    elif num<base:
        return False
    elif num%base == 0:
        return is_power(num//base, base)
    return False


