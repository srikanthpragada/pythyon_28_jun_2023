gv = 1000

def f1():
    ev = 100
    global  gv
    gv = 0
    def f2():
        lv = 10
        nonlocal ev
        ev = 1
        print(lv, ev, gv)

    f2()
    print(ev, gv)


f1()
