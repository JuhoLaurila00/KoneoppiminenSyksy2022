
def create():
    lista = ["a","b","c"]
    tuple = (1, 2, 3)
    s = set()

    s.add(5)
    s.add(6)
    s.add(4)
    
    dict= {}
    dict[7] = "Seven"
    dict[8] = "Eight"
    dict[9] = "Nine"


    print(lista[1])
    print(tuple[1])

    x = list(s).pop(1)
    print(x)
    
    y = list(dict).pop(1)
    print(y)

create()
