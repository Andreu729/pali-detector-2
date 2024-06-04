# xax  - xx

def element_deleter(list_, pos):
    mod_list = []
    i = 0
    for e in list_:
        if not (i == pos):
            mod_list.append(e)
        i += 1
    return mod_list
