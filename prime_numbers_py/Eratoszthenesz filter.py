def prog():
    import math
    import datetime
    t1 = datetime.datetime.now()
    n = int(input("Upper limit for the investigation: "))
    lst = [True]*n                      # create a list with n pcs elements
    for i in range(2,int(math.sqrt(n))):     # map the list from index 2 till the square root of the upper limit
        for j in range(i*i, n, i):      # for thoose elements in the list what index is multiplier for the i, attach 'FALSE'
            lst[j] = False
#"""
    for i in range(2,n):                # print the remaining 'TRUE' value's indexes
        if lst[i]:
            print(i)
    t2 = datetime.datetime.now()
    print((t2-t1).seconds, "sec needed for the computing.")
#"""
    c = int(input("Which number are you interested? >>> "))
    if lst[c] == True:
        print("A " + str(c) + " is a prime!")
    else:
        print("A " + str(c) + " is not a prime!")

    valasz = input("An other round? y/n >>> ")
    if valasz == 'y':
        prog()
prog()
