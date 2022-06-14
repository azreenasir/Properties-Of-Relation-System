# IMPORT PYTHON LIBRARY
from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import sys


# FUNCTION FOR TRANSITIVE
def is_transitive(set, relation):
    for i in set:
        for j in set:
            for k in set:
                if ((i, j) in relation and (j, k) in relation) and (not (i, k) in relation):
                    return False
                if(len(relation) == 1):
                    return False
    return True

# FUNCTION FOR SYMMETRIC
def is_symmetric(relation):
    # checks symmetric property: (a, b) -> (b, a)
    return all(rel[::-1] in relation for rel in relation)

# FUNCTION FOR REFLEXIVE
def is_reflexive(relation, set):
    for a in set:
        if (a,a) not in relation:
            return False
    return True


# FUNCTION TO CHECK THE CONDITION IF IT IS TRUE THEN RETURN SYMMETRIC
def check_symmetric(relation):
    if (is_symmetric(relation)== True):
        return 'symmetric'
    if (is_symmetric(relation) == False):
        return 'not symmetric'

# FUNCTION TO CHECK THE CONDITION IF IT IS TRUE THEN RETURN TRANSITIVE
def check_transitive(set, relation):
    if (is_transitive(set, relation) == True):
        return 'transitive'
    if (is_transitive(set, relation) == False):
        return 'not transitive'
    if (is_transitive(set, relation) == len(relation)):
        return 'Only 1 element given'

# FUNCTION TO CHECK THE CONDITION IF IT IS TRUE THEN RETURN REFLEXIVE
def check_reflexive(relation, set):
    if (is_reflexive(relation, set) == True):
        return 'reflexive'
    if (is_reflexive(relation, set) == False):
        return 'not reflexive'

# FUNCTION FOR OUTPUT THE RESULT OF ALL CONDITION
def check_all(relation, set):
    global LabelResult
    relation = eval(relation)
    set = eval(set)
    LabelResult = Label(frame, 
                    text="The Set is " + 
                    check_reflexive(relation, set) + 
                    ", " + 
                    check_symmetric(relation) + 
                    " and " +
                    check_transitive(set, relation), 
                    font="Arial 20 bold",
                    bg="#509ed8")
    LabelResult.place(relx=0.31, rely=0.52)

# FUNCTION PROVE IT IS NOT REFLEXIVE
def if_not_reflexive(relation, domain):
    global LabelReflexive
    relation = eval(relation)
    domain = eval(domain)
    if(check_reflexive(relation, domain) == "not reflexive"):
        closure = set(relation)
        new_closure = set()
        while True:
            new_relations = set((x,x) for x in domain if x==x)
            closure_until_now = new_relations
            new_closure = closure_until_now
            result = new_closure.difference(closure)
            break

        LabelReflexive = Label(frame,
                        text="Its not reflexive because it doesn't contain " + str(result),
                        font="Arial 20 bold",bg="#509ed8")
        LabelReflexive.place(relx=0.25, rely=0.6)

# FUNCTION TO PROVE IT IS NOT TRANSITIVE
def if_not_transitive(relation, domain):
    global LabelTransitive
    relation = eval(relation)
    domain = eval(domain)
    if(check_transitive(domain, relation ) == "not transitive"):
        closure = set(relation)
        new_closure = set()
        while True:
            new_relations = set((x,w) for x,y in closure for q,w in closure if q == y)
            closure_until_now = new_relations
            new_closure = closure_until_now
            result = new_closure.difference(closure)
            break

        LabelTransitive = Label(frame,
                         text="Its not transitive because it doesn't contain " + str(result),
                         font="Arial 20 bold",bg="#509ed8")
        LabelTransitive.place(relx=0.25, rely=0.65)

        if(len(result) == 0):
                result = "Its not transitive because only 1 element given"
                LabelTransitive.config(text=result)

# FUNCTION TO PROVE IT IS NOT SYMMETRIC
def if_not_symmetric(relation):
    global LabelSymmetric
    relation = eval(relation)
    if(check_symmetric(relation) == "not symmetric"):
        closure = set(relation)
        new_closure = set()
        while True:
            new_relations = set((x,y) for x,y in closure for (y,x) in closure if (x==x and y==y))
            closure_until_now = new_relations
            new_closure = closure_until_now
            result = new_closure.difference(closure)
            break

        LabelSymmetric = Label(frame, 
                        text="Its not symmetric because it doesn't contain " + str(result), 
                        font="Arial 20 bold",bg="#509ed8")
        LabelSymmetric.place(relx=0.25, rely=0.7)

# FUNCTION TO CLEAR THE RESULT
def remove_text():
	LabelResult.config(text="")

# FUNCTION TO CLEAR THE RESULT FOR ALL
def remove_prove():
    LabelReflexive.config(text="")
    LabelTransitive.config(text="")
    LabelSymmetric.config(text="")

# GUI CODING

# Create Windows, Title and Size of the Windows
root = tk.Tk()
root.title('PROJECT CSC510!')
root.geometry("1920x1080")
root.withdraw()
root.iconbitmap("icon.ico")

# Create New Windows for Welcome Page
welcome = tk.Tk()
welcome.title("Welcome Page!!")
welcome.geometry("700x500")
welcome.iconbitmap("icon.ico")

#################################################################

# WELCOME WINDOWS GUI

# Frame For Welcome Page
framewelcome = tk.Frame(welcome, bg="#509ed8")
framewelcome.place(relwidth=1, relheight=1)

# Label For Welcome Page 
Labelwelcome = Label(welcome, text="WELCOME TO OUR PROJECT CSC510!", font="SimSun 24 bold", bg="#8cd5ff", borderwidth=2, relief="raised")
Labelwelcome.place(relx=0.14, rely=0.1)

# Button to display the System
Buttonshow = Button(welcome, text="Run Application", font="Arial, 12",padx=20,pady=10,fg="white",bg="#263d4d", command= lambda: [root.deiconify(), welcome.destroy()])
Buttonshow.place(relx= 0.4, rely=0.6)

# Button to exit program from welcome screen
ButtonExit = Button(welcome, text="Exit", font="Arial, 12",padx=20,pady=10,fg="white",bg="#263d4d", command= lambda: [welcome.destroy(), root.destroy()])
ButtonExit.place(relx=0.85, rely=0.85)

# label to summarise what this apps do
LabelSummary = Label(welcome, 
                text="This application can prove whether the relation \n is reflexive, symmetric or transitive.\n It also explains why the relation\n is not reflexive, symmetric or transitive.", 
                font="Ebrima 18 bold", bg="#D4F1F4" )
LabelSummary.place(relx=0.1, rely=0.25)

#################################################################

# SYSTEM WINDOWS GUI

# Frame For System Page
frame =tk.Frame(root,bg="#509ed8")
frame.place(relwidth=0.9, relheight=0.85, relx=0.05, rely=0.05)

# Title 
labelTitle = Label(frame, text="Properties Of Relation System", font="Arial 40 bold", background="#e5f0f1", borderwidth=2, relief=SOLID)
labelTitle.place(relx=0.27, rely=0.05)

# Label for Input Set of Element
LabelSet = Label(frame, text="Insert the Set of Element", font="Arial 20 bold", bg="#509ed8")
LabelSet.place(relx=0.4, rely=0.16)

# Label for Input Set of Relations
LabelRelation = Label(frame, text="Insert the Relations", font="Arial 20 bold", bg="#509ed8")
LabelRelation.place(relx=0.42, rely=0.26)

# Input Set to insert the set
InputSet = tk.Entry(frame, font="Arial, 20")
InputSet.place(relx=0.21, rely=0.2,width=1000, height=40)

# Input Relations to insert the set
InputRelations = tk.Entry(frame, font="Arial, 20")
InputRelations.place(relx=0.21, rely=0.3,width=1000, height=40)

# Button for display the result
RunSet = tk.Button(frame,text="Get The Result", font="Arial, 12",padx=20,pady=10,fg="white",bg="#263D42", 
                    command=lambda: 
                    [remove_text(),
                    remove_prove(),
                    check_all(InputRelations.get(), InputSet.get()),
                    if_not_reflexive(InputRelations.get(), InputSet.get()),
                    if_not_transitive(InputRelations.get(), InputSet.get()),
                    if_not_symmetric(InputRelations.get())
                    ])
RunSet.place(relx= 0.458, rely=0.35)

# Label Result
LabelResult = Label(frame,text="",bg="#509ed8")
LabelResult.place(relx=0.4, rely=0.5)

# Label to prove if its not reflexive
LabelReflexive = Label(frame, text="", bg="#509ed8")
LabelReflexive.place(relx=0.25, rely=0.6)

# Label to prove if its not transitive
LabelTransitive = Label(frame, text="",bg="#509ed8")
LabelTransitive.place(relx=0.25, rely=0.65)

LabelSymmetric = Label(frame, text="",bg="#509ed8")
LabelSymmetric.place(relx=0.25, rely=0.7)

# Output Label
LabelOutput = tk.Label(frame, text="Result", font="Arial 20 bold", bg="#509ed8")
LabelOutput.place(relx=0.475, rely=0.45)

# Reset Button to clear Label Output
ResetButton = Button(frame, text="Clear Result", font="Arial, 12",padx=20,pady=10,fg="white",bg="#263d4d", 
                    command= lambda: [remove_text(), 
                             remove_prove()])
ResetButton.place(relx=0.815, rely=0.9)

# Exit Button
Exitbutton = Button(frame, text = "Exit!",font="Arial, 12",padx=20,pady=10,fg="white",bg="#263d4d", command = root.destroy)
Exitbutton.place(relx=0.9, rely=0.9)

# Logo Discrete
path = "logo.jpg"
img = Image.open(path)
resized = img.resize((200,200), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resized)

# Label For Discrete Logo
labelLogo = tk.Label(frame, image = logo, bg="#509ed8")
labelLogo.place(relx=0.01, rely=0.02)

# Logo UITM
path = "uitm.jpg"
img = Image.open(path)
resized = img.resize((200,200), Image.ANTIALIAS)
uitm = ImageTk.PhotoImage(resized)

# Label For UITM Logo
labelUITM = tk.Label(frame, image = uitm, bg="#509ed8")
labelUITM.place(relx=0.872, rely=0.02)

mainloop()

#################################################################



#{(1,2), (1,3), (2,3), (2,1), (2,2), (3,2), (3,3), (1,1)}