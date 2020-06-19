# Logikai játék

import random, sys

#select language

lang = input("Kérlek válasz nyelvet! / Please select language! [hu/en] >>> ")

# instruction about rules
if lang == 'hu':
    print ('\nAz A,B,C,D,E,F elemekből álló sort kell megfelelő sorrendben eltalálni.\n'
        'Szóköz nélkül kell begépelni a karaktereket.\n'
        'Egy elem csak egyszer szerepel.\nFekete pálcika [×] jelzi a helyes elemet, de rossz helyen;\n'
        'Fehér pálcika [o] a helyes elemet jó helyen.\n'
        'A pálcikák sorrendje nincs összefüggésben az elemek sorrendjével.\n'
        "A játék befejezéséhez gépeld be hogy 'exit'!\n")
if lang == 'en':
    print ('\nYou should figure out the ordered list what contains A,B,C,D,E,F elements.\n'
        'Type the characters without space.\n'
        'A character occurs once in the list.\nBlack marker [×] indicates the correct color but on wrong place;\n'
        'White marker [o] indicates the right color on right place.\n'
        'The order of the markers is indepentent from the order of the elements what they refers.\n'
        "To finish the game, type 'exit'!\n")

# puzzle
i = 0
inventory = ['A','B','C','D','E','F']
code = []
while i != 4:
    a = random.choice(inventory)
    inventory.remove(a)
    code.append(a)
    i += 1

print("\t\t[?] [?] [?] [?]")
#print(code)

counter = 1
while counter > 0:
    answ = []
    if lang == 'hu':
        proba = input(str(counter)+". próba >>> ")
    if lang == 'en':
        proba = input(str(counter)+". try >>> ")
    if proba == 'exit':
        if lang == 'hu':
            print("\nKöszönöm a játékot!")
        if lang == 'en':
            print("\nThank you for the game!")
        sys.exit()
    proba = list(proba.upper())
    if len(proba) == 4:  
        k = 0
        for c in proba:
            if c == code[k]:
                answ.append('o')
            elif c in code:
                answ.append('×')
            z=1
            k += 1
        if answ == ['o','o','o','o']:
            if lang == 'hu':
                print("\t\t\tGratulálok! Győztél! " +str(counter)+" kör alatt kitaláltad.")
            if lang == 'en':
                print("\t\t\tCongratulation! You win! Figured out in " +str(counter)+" try.")
            sys.exit()
        answ=sorted(answ)
        print("\t\t\t",*answ)
        counter += 1
    else:
        if lang == 'hu':
            print("Négy elemet kell megadni!")
        if lang == 'en':
            print("Please provide four elements!")
#print(proba)


