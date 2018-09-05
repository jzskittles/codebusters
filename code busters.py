from Tkinter import *
import string
import numpy as np

master = Tk()
master.title("Code Busters Solver")
master.configure(background="white")

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index

key = StringVar()
phrase = StringVar()
v = IntVar()
affinea = StringVar()
affineb = StringVar()
phrasenum = []
keynum = []
solnum = []
solution = StringVar()
solution.set("")
labell = StringVar()
labell.set("")

def mon():
    framemono.pack( side = TOP )
    framevig.pack_forget()
    frameaff.pack_forget()
    phrase.set("")
    key.set("")
    affinea.set("")
    affineb.set("")
    solution.set("")
    buttons.configure(command=mono)
    print "solve mono"

def vig():
    framemono.pack( side = LEFT )
    framevig.pack( side = LEFT )
    frameaff.pack_forget()
    phrase.set("")
    key.set("")
    affinea.set("")
    affineb.set("")
    solution.set("")
    buttons.configure(command = vigenere)
    print "solve vig"

def aff():
    framemono.pack(side = LEFT)
    framevig.pack_forget()
    frameaff.pack(side = LEFT)
    phrase.set("")
    key.set("")
    affinea.set("")
    affineb.set("")
    solution.set("")
    buttons.configure(command = affine)
    print "solve aff"

def hil():
    framemono.pack( side = LEFT )
    framevig.pack( side = LEFT )
    frameaff.pack_forget()
    phrase.set("")
    key.set("")
    affinea.set("")
    affineb.set("")
    solution.set("")
    buttons.configure(command = hill)
    print "solve hill"

def mono():
    labell.set("")
    print "solve mono"

def vigenere():
    del solnum[:]
    del phrasenum[:]
    del keynum[:]
    
    for letter in phrase.get():
        phrasenum.append(values[letter])
    for letter in key.get():
        keynum.append(values[letter])
    
    if v.get() != 2:
        solution.set("")
        labell.set("")

        count=0
        for letter in phrasenum:
            if v.get() == 0:
                solnum.append((letter-keynum[count%(len(keynum))])%26)
            if v.get() == 1:
                solnum.append((letter+keynum[count%(len(keynum))])%26)
            count+=1
        solution.set("")

        for letter in solnum:
            for let in values:
                if values[let] == letter:
                    solution.set(solution.get()+let)
    else:
        for letter in solution.get():
            solnum.append(values[letter])
        if len(solution.get()) != 0:
            if len(phrasenum) == 0:
                labell.set("use decode function instead")
                print "missing phrase"
            if len(keynum) == 0:
                count=0
                for letter in phrasenum:
                    keynum.append((solnum[count]-letter)%26)
                    count+=1
                labell.set("missing key")
                for letter in keynum:
                    for let in values:
                        if values[let] == letter:
                            key.set(key.get()+let)
                print "missing key"
        else:
            labell.set("cannot solve, put in solution")

def affine():
    del solnum[:]
    del phrasenum[:]
    affineinverse = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
    
    for letter in phrase.get():
        phrasenum.append(values[letter])

    if v.get() != 2:
        solution.set("")
        labell.set("")

        aa = int(affinea.get() or 0)
        bb = int(affineb.get() or 0)
        for letter in phrasenum:
            if v.get() == 0:
                for inv in affineinverse:
                    if inv == aa:
                        solnum.append((affineinverse[inv]*(letter-bb))%26)
            if v.get() == 1:
                solnum.append((aa*letter+bb)%26)
        for letter in solnum:
            for let in values:
                if values[let] == letter:
                    solution.set(solution.get()+let)
    else:
        for letter in solution.get():
            solnum.append(values[letter])
        print solnum
        if len(solution.get()) != 0:
            if len(phrasenum) == 0:
                labell.set("use decode function instead")
                print "missing phrase"
            aa = int(affinea.get() or 0)
            bb = int(affineb.get() or 0)
            if aa == 0 and bb == 0:
                labell.set("missing a and b")

                inversea = 0
                for inv in affineinverse:
                    inversea = affineinverse[inv]
                    count = 0
                    newa = 0
                    newb = 0
                    countyay = 0
                    for letter in phrasenum:
                        for num in range(1,26):
                            if(phrasenum[count]-(inversea*(solnum[count]-num))%26)==0:
                                if(newa == inversea and newb == num):
                                    print "yay!!!!!"
                                    countyay+=1
                                    if countyay == len(solution.get())-1:
                                        affinea.set(inv)
                                        affineb.set(newb)         
                                else:
                                    countyay = 0
                                    newa = inversea
                                    newb = num
                        count+=1                                          
            elif aa > 0 or bb > 0:
                if aa > 0:
                    inversea = 0
                    for inv in affineinverse:
                        if inv == aa:
                            inversea = affineinverse[inv]
                            break
                    count=0
                    for letter in phrasenum:
                        for num in range(1, 26):
                            if (phrasenum[count] - (inversea*(solnum[count]-num))%26)==0:
                                affineb.set(num)
                                break
                        count+=1
                    labell.set("missing b")
                else:
                    inversea = 0
                    count=0
                    for num in range(1,26):
                        if (num*(solnum[count] - bb))%26 == phrasenum[count]:
                            for inv in affineinverse:
                                if inv == num:
                                    affinea.set(affineinverse[inv]);
                                    count+=1
                                    break
                    labell.set("missing a")
        else:
            labell.set("cannot solve, put in solution")

def hill():    
    del solnum[:]
    del phrasenum[:]
    del keynum[:]
    
    for letter in phrase.get():
        phrasenum.append(values[letter])
    for letter in key.get():
        keynum.append(values[letter])
    
    if v.get() != 2:
        solution.set("")
        labell.set("")

        if v.get() == 1:
            keymatrix = []
            if len(keynum) == 4:
                keymatrix = [[keynum[0],keynum[1]],
                            [keynum[2],keynum[3]]]
                phrasematrix = []
                lettermatrix = []
                count = 0
                for letter in phrasenum:
                    if count%2==0:
                        lettermatrix = []
                        lettermatrix.append(letter)
                        count+=1
                        if count == len(phrasenum):
                            lettermatrix.append(25)
                            phrasematrix.append(lettermatrix)
                    else:
                        lettermatrix.append(letter)
                        phrasematrix.append(lettermatrix)
                        count+=1
                #print phrasematrix
                #print keymatrix
            elif len(keynum) == 9:
                keymatrix = [[keynum[0],keynum[1],keynum[2]],
                            [keynum[3],keynum[4],keynum[5]],
                            [keynum[6],keynum[7],keynum[8]]]
                phrasematrix = []
                lettermatrix = []
                count = 0
                for letter in phrasenum:
                    if count%3==0:
                        lettermatrix.append(letter)
                        count+=1
                        if count == len(phrasenum):
                            lettermatrix.append(25)
                            lettermatrix.append(25)
                            phrasematrix.append(lettermatrix)
                    elif count%3==1:
                        lettermatrix.append(letter)
                        count+=1
                        if count == len(phrasenum):
                            lettermatrix.append(25)
                            phrasematrix.append(lettermatrix)
                    else:
                        lettermatrix.append(letter)
                        phrasematrix.append(lettermatrix)
                        count+=1
                        lettermatrix = []
            else:
                labell.set("Incorrect number of characters for key!!")
            sol = []
            for subpart in phrasematrix:
                sol.append(np.matmul(keymatrix, subpart).tolist())
            for section in sol:
                for item in section:
                    item = item%26
                    for let in values:
                        if values[let] == item:
                            solution.set(solution.get()+let)
            
            
            """for letter in phrasenum:
                if v.get() == 0:
                    solnum.append((letter-keynum[count%(len(keynum))])%26)
                if v.get() == 1:
                    solnum.append((letter+keynum[count%(len(keynum))])%26)
                count+=1
            solution.set("")

            for letter in solnum:
                for let in values:
                    if values[let] == letter:
                        solution.set(solution.get()+let)
        else:
            for letter in solution.get():
                solnum.append(values[letter])
            if len(solution.get()) != 0:
                if len(phrasenum) == 0:
                    labell.set("use decode function instead")
                    print "missing phrase"
                if len(keynum) == 0:
                    count=0
                    for letter in phrasenum:
                        keynum.append((solnum[count]-letter)%26)
                        count+=1
                    labell.set("missing key")
                    for letter in keynum:
                        for let in values:
                            if values[let] == letter:
                                key.set(key.get()+let)
                    print "missing key"
            else:
                labell.set("cannot solve, put in solution")"""

def affine():
    del solnum[:]
    del phrasenum[:]
    affineinverse = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
    
    for letter in phrase.get():
        phrasenum.append(values[letter])

    if v.get() != 2:
        solution.set("")
        labell.set("")

        aa = int(affinea.get() or 0)
        bb = int(affineb.get() or 0)
        for letter in phrasenum:
            if v.get() == 0:
                for inv in affineinverse:
                    if inv == aa:
                        solnum.append((affineinverse[inv]*(letter-bb))%26)
            if v.get() == 1:
                solnum.append((aa*letter+bb)%26)
        for letter in solnum:
            for let in values:
                if values[let] == letter:
                    solution.set(solution.get()+let)
    print "solve hill"

container = Frame(master)
container.pack()

label = Label(container, text="What type of cipher?")
label.pack(side = TOP)

buttonm = Button(container, text="Monoalphabetic", command = mon)
buttonm.pack(side = LEFT)

buttonv = Button(container, text="Vigenere", command = vig)
buttonv.pack(side = LEFT)

buttona = Button(container, text="Affine", command = aff)
buttona.pack(side = LEFT)

buttonh = Button(container, text="Hill", command = hil)
buttonh.pack(side = LEFT)

framemono = Frame(master)
labelp = Label(framemono, text="Phrase: ")   
labelp.pack(side = LEFT)
vphrase = Entry(framemono, width=25, textvariable=phrase)
vphrase.pack(side = TOP)

framevig = Frame(master)
labelk = Label(framevig, text="Key:")
labelk.pack(side = LEFT)
vkey = Entry(framevig, width=16, textvariable=key)
vkey.pack(side = LEFT)

frameaff = Frame(master)
labela = Label(frameaff, text="A: ")
labela.pack(side = LEFT)
va = Entry(frameaff, width=7, textvariable=affinea)
va.pack(side = LEFT)
labelb = Label(frameaff, text="B: ")
labelb.pack(side = LEFT)
vb = Entry(frameaff, width=7, textvariable=affineb)
vb.pack(side = LEFT)

framesol = Frame(master)
framesol.pack(side = BOTTOM)

framesolution = Frame(framesol)
framesolution.pack()
labels = Label(framesolution, text="Solution: ")
labels.pack(side = LEFT)
soltext = Entry(framesolution, textvariable=solution)
soltext.pack(side = LEFT)

framecontext = Frame(framesol)
framecontext.pack(side = BOTTOM)
labelall = Label(framecontext, textvariable = labell)
labelall.pack(side = BOTTOM)

frameradio = Frame(master)
frameradio.pack(side = BOTTOM)
drbutton = Radiobutton(frameradio, text="Decode", variable=v, value=0)
erbutton = Radiobutton(frameradio, text="Encode", variable=v, value=1)
nokeybutton = Radiobutton(frameradio, text="Unknown Key/A/B", variable=v, value=2)
drbutton.pack(side = LEFT)
erbutton.pack(side = LEFT)
nokeybutton.pack(side = LEFT)

buttons = Button(frameradio, text="Solve", command = mono)
buttons.pack(side = BOTTOM)

master.mainloop()
