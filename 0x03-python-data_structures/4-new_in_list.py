#!/usr/bin/python3
#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at a specific position without modifying original"""
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy