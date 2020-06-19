# prím számok kilistázása / prime numbers listing

import datetime
t1 = datetime.datetime.now()
a = int(input("Upper limit for the investigation: "))
c = 2
list = []

while c <= a:
    b = 1
    k = 0
    while c >= b:
        if c%b == 0:
            k += 1
        b += 1
    if k == 2:
        list.append(c)
        print(c)
    c += 1
    
#print(*list, sep = "\n")
t2 = datetime.datetime.now()
#print((t2-t1).seconds, "sec needed for creating the list.")

