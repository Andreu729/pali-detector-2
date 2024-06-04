# xax  - xx

def element_deleter(list_, pos):
    mod_list = []
    i = 0
    for e in list_:
        if not (i == pos):
            mod_list.append(e)
        i += 1
    return mod_list


def odd_deleter(a):
    if len(a) % 2 == 1:
        pos = (len(a)-1)/2
        al = list(a)
        fl = element_deleter(al, pos)
        return "".join(fl)
    else:
        return a
