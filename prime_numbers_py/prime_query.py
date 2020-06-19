# the given number is a prime?

#ver1
c = int(input("Pick a number! >>> "))

b = 1
k = 0
while c >= b:
    if c%b == 0:
        k += 1
    b += 1
    #print(b)
if k == 2:
    print("A " + str(c) + " is a prime!")
else:
    print("A " + str(c) + " is not a prime!")

#ver2
c = int(input("Pick a number! >>> "))

if (2**(c-1))%c==1:
    print("A " + str(c) + " is a prime!")
else:
    print("A " + str(c) + " is not a prime!")
question = input(":)")
