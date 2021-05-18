from tkinter import *
import random
import tkinter.messagebox as tmsg


words = ["dilhe","npue","naatp","manatpkhasiav","draaadov","adbreahdy","adbedamha","nianehc","upairj","uprank"]
answer = ["delhi","pune","patna","visakhapatnam","vadodara","hyderabad","ahmedabad","chennai","jaipur","kanpur"]


root = Tk()
root.title("Jamball Words ")

num = random.randrange(0,11,1)

def result():
    global num,answer,words
    label.config(text=words[num])

def check():
    global num,answer,words
    var = ans.get()
    if var == answer[num]:
        tmsg.showinfo("success","you have gussed the right answer")
        entry.delete(0,END)
        res()
        
        
    else:
        tmsg.showerror("error","this is not the correct answer")
        entry.delete(0,END)
        res()
       

def res():
    global num,answer,words
    num = random.randrange(0,11,1)
    label.config(text=words[num])
    entry.delete(0,END)



# here in geomtery after setting the it 600+210 is used to open the GUI in the middle of the screen
root.geometry("300x370+600+210")

root.minsize(299, 369)
root.maxsize(301, 371)

# Root.configure is used to change the background of the GUI
root.configure(background="black")




label = Label(root,text="question",bg="black",font="comicsansms 25",fg="white",pady=15)
label.pack()


ans = StringVar()
entry=Entry(root,text=ans,font="comicsansms 15")
entry.pack(pady=5)

button1 = Button(root,text="Check",font="comicsansms 15",padx=10,pady=7,bg = "grey",fg="#F4C724",border="0",command=check)
button1.pack(pady=15)

button2 = Button(root,text="Reset",font="comicsansms 15",padx=10,pady=7,bg = "grey",fg="#F4C724",border="0",command=res)
button2.pack(pady=15)

result()

root.mainloop()
