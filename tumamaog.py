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



def splitter(stri):
    p = len(stri)/2
    l1 = []
    l2 = []
    lstr = list(stri)
    i = 0
    for e in lstr:
        if i < p:
            l1.append(e)
        else:
            l2.append(e)
        i += 1
    return [l1, l2]


def reverser(list_):
    victim = list_[1]
    rlist = []
    p = len(victim) - 1
    for a in range(0, p + 1):
        rlist.append(victim[p])
        p -= 1
    return rlist


def pal_detect(s):
    s = odd_deleter(s)
    sl = splitter(s)
    sr = reverser(sl)
    if sl[0] == sr:
        return True
    else:
        return False


print("Bienvenido al pali detector!")
print("Escribe una palabra y revisaremos si es palíndromo:")
xd = input("Escribe una palabra: ")
if pal_detect(xd):
    print(xd + " es un palíndromo!")
else:
    print("muerete pedazo de basura")
