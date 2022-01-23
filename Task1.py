f = open("mat_dv2-2.txt", "r")
l = list()
for i in f:
    l = i.split()
    print(l)
    if l[2] == 8:
        print(l)
    
