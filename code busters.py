from Tkinter import *
import string

master = Tk()
master.title("Code Busters Solver")
master.configure(background="white")

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    if index not in values:
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
cat = StringVar()
cat.set("")
catb = StringVar()
catb.set("")



def raise_frame(frame):
    frame.tkraise()

def mono():
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

def getvigenere():
    labelp = Label(master, text="Phrase: ").grid(column=0, row=2, sticky="W")    
    vphrase = Entry(master, width=25, textvariable=phrase)
    vphrase.grid(row=3, column=0, columnspan=2)
    cat.set("Key:")
    catb.set("")
    labelk = Label(master, textvariable=cat).grid(column=2, row=2, sticky="W")
    vkey = Entry(master, width=16, textvariable=key)
    vkey.grid(row=3, column=2, columnspan=2)
    drbutton = Radiobutton(master, text="Decode", variable=v, value=0).grid(column=0, row=4, sticky="W")
    erbutton = Radiobutton(master, text="Encode", variable=v, value=1).grid(column=1, row=4, sticky="W")

    buttons = Button(master, text="Solve", command = vigenere)
    buttons.grid(row=5, column=0)    

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

def getaffine():
    labelp = Label(master, text="Phrase: ").grid(column=0, row=2, sticky="W")    
    vphrase = Entry(master, width=25, textvariable=phrase)
    vphrase.grid(row=3, column=0, columnspan=2)
    cat.set("A: ")
    labela = Label(master, textvariable=cat).grid(column=2, row=2, sticky="W")
    va = Entry(master, width=7, textvariable=affinea)
    va.grid(row=3, column=2)
    catb.set("B: ")
    labelb = Label(master, textvariable=catb).grid(column=3, row=2, sticky="W")
    vb = Entry(master, width=7, textvariable=affineb)
    vb.grid(row=3, column=3)
    drbutton = Radiobutton(master, text="Decode", variable=v, value=0).grid(column=0, row=4, sticky="W")
    erbutton = Radiobutton(master, text="Encode", variable=v, value=1).grid(column=1, row=4, sticky="W")

    buttons = Button(master, text="Solve", command = affine)
    buttons.grid(row=5, column=0)

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

def gethill():
    labelp = Label(master, text="Phrase: ").grid(column=0, row=2, sticky="W")    
    vphrase = Entry(master, width=25, textvariable=phrase)
    vphrase.grid(row=3, column=0, columnspan=2)
    cat.set("Key:")
    catb.set("")
    labelk = Label(master, textvariable=cat).grid(column=2, row=2, sticky="W")
    vkey = Entry(master, width=16, textvariable=key)
    vkey.grid(row=3, column=2, columnspan=2)
    drbutton = Radiobutton(master, text="Decode", variable=v, value=0).grid(column=0, row=4, sticky="W")
    erbutton = Radiobutton(master, text="Encode", variable=v, value=1).grid(column=1, row=4, sticky="W")

    buttons = Button(master, text="Solve", command = hill)
    buttons.grid(row=5, column=0)

def hill():
    print "solve hill"

container = Frame(master)
container.pack()

label = Label(container, text="What type of cipher?")#.grid(column=0, row=0)
label.pack(side = TOP)

buttonm = Button(container, text="Monoalphabetic", command = mono)
#buttonm.grid(row=1, column=0)
buttonm.pack(side = LEFT)

buttonv = Button(container, text="Vigenere", command = vig)
#buttonv.grid(row=1, column=1)
buttonv.pack(side = LEFT)

buttona = Button(container, text="Affine", command = aff)
#buttona.grid(row=1, column=2)
buttona.pack(side = LEFT)

buttonh = Button(container, text="Hill", command = hil)
#buttonh.grid(row=1, column=3)
buttonh.pack(side = LEFT)

"""for child in master.winfo_children():
    child.grid_configure(padx=5, pady=5)"""

#master.bind('<Return>', solve)

framemono = Frame(master)
labelp = Label(framemono, text="Phrase: ")#.grid(column=0, row=2, sticky="W")    
labelp.pack(side = LEFT)
vphrase = Entry(framemono, width=25, textvariable=phrase)
vphrase.pack(side = TOP)
#vphrase.grid(row=3, column=0, columnspan=2)

framevig = Frame(master)
labelk = Label(framevig, text="Key:")#.grid(column=2, row=2, sticky="W")
labelk.pack(side = LEFT)
vkey = Entry(framevig, width=16, textvariable=key)
vkey.pack(side = LEFT)

frameaff = Frame(master)
labela = Label(frameaff, text="A: ")#.grid(column=2, row=2, sticky="W")
labela.pack(side = LEFT)
va = Entry(frameaff, width=7, textvariable=affinea)
va.pack(side = LEFT)
labelb = Label(frameaff, text="B: ")#.grid(column=3, row=2, sticky="W")
labelb.pack(side = LEFT)
vb = Entry(frameaff, width=7, textvariable=affineb)
vb.pack(side = LEFT)

frameradio = Frame(master)
frameradio.pack(side = BOTTOM)
drbutton = Radiobutton(frameradio, text="Decode", variable=v, value=0)#.grid(column=0, row=4, sticky="W")
erbutton = Radiobutton(frameradio, text="Encode", variable=v, value=1)#.grid(column=1, row=4, sticky="W")
drbutton.pack(side = LEFT)
erbutton.pack(side = LEFT)

buttons = Button(frameradio, text="Solve", command = mono)
buttons.pack(side = BOTTOM)
#buttons.grid(row=5, column=0)

master.mainloop()
#uphrase = raw_input("which type")
