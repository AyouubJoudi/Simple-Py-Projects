choice = True
while choice:
        while True:
                op = input("""
please enter an operation without spaces:
""")
                if op.find(" ") == -1:
                        break
        a = op.find("+")
        b = op.find("-")
        c = op.find("*")
        d = op.find("/")
        e = op.find("//")
        f = op.find("%")
        g = op.find("**")
        if a != -1:
                print(int(op[:a])+int(op[a+1:]))
        elif b != -1:
                print(int(op[:b])-int(op[b+1:]))
        elif c != -1 and g == -1:
                print(int(op[:c])*int(op[c+1:]))
        elif d != -1 and e == -1:
                print(int(op[:d])/int(op[d+1:]))
        elif e != -1:
                print(int(op[:e])//float(op[e+2:]))
        elif f != -1:
                print(int(op[:f]) % int(op[f+1:]))
        elif g != -1:
                print(int(op[:g])**int(op[g+2:]))
        p = input("try again(Yes/No) ")
        if p.upper() == "YES":
                print("ok")
        else:
                print("bye :(")
                choice = False

            
