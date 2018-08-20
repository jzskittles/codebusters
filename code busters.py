from Tkinter import *
import string

master = Tk()
master.title("Code Busters Solver")
master.configure(background="white")

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index

key = StringVar()
phrase = StringVar()
v = IntVar()
affinea = IntVar()
affineb = IntVar()
phrasenum = []
keynum = []
solnum = []
solution = StringVar()
solution.set("")

def mon():
    framemono.pack( side = TOP )
    framevig.pack_forget()
    frameaff.pack_forget()
    buttons.configure(command=mono)
    print "solve mono"

def vig():
    framemono.pack( side = LEFT )
    framevig.pack( side = LEFT )
    frameaff.pack_forget()
    buttons.configure(command = vigenere)
    print "solve vig"

def aff():
    framemono.pack(side = LEFT)
    framevig.pack_forget()
    frameaff.pack(side = LEFT)
    buttons.configure(command = affine)
    print "solve aff"

def hil():
    framemono.pack( side = LEFT )
    framevig.pack( side = LEFT )
    frameaff.pack_forget()
    buttons.configure(command = hill)
    print "solve hill"

def mono():
    print "solve mono"

def vigenere():
    del solnum[:]
    del phrasenum[:]
    del keynum[:]
    solution.set("")
    
    for letter in phrase.get():
        phrasenum.append(values[letter])
    for letter in key.get():
        keynum.append(values[letter])
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
    print solution.get()
    print "solve vigenere"

def affine():
    del solnum[:]
    del phrasenum[:]
    solution.set("")
    aa = affinea.get()
    bb = affineb.get()
    affineinverse = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
    for letter in phrase.get():
        phrasenum.append(values[letter])
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
    print solution.get()
    print "solve affine"

def hill():
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

frameradio = Frame(master)
frameradio.pack(side = BOTTOM)
drbutton = Radiobutton(frameradio, text="Decode", variable=v, value=0)
erbutton = Radiobutton(frameradio, text="Encode", variable=v, value=1)
drbutton.pack(side = LEFT)
erbutton.pack(side = LEFT)

buttons = Button(frameradio, text="Solve", command = mono)
buttons.pack(side = BOTTOM)

master.mainloop()
