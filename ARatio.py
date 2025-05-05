from tkinter import *
from tkinter import messagebox

text_color = "#F9627D"
entry_color = "#f53614"
background_color = "#55868C"
bg_again = "#6153CC"
entry_bg_color = "#9153C1"
#width = 1920, height = 1080

num1 = "1 gazillion"
asp1 = 16
asp2 = 9

def math(event):
    global num1
    global asp1
    global asp2
    
    asp1 = int(entryASP1.get())
    asp2 = int(entryASP2.get())
    
    num1 = asp1*int(entry.get())/asp2
    label.config(text=f"Out: {num1}")
    math_label.config(text=f"Math: {asp1} × {int(entry.get())} ÷ {asp2}")

def change_asp(event):
    global asp1
    global asp2
    asp1 = int(entryASP1.get())
    asp2 = int(entryASP2.get())



#Window
window = Tk()
window.config(bg=background_color)
window.title("Aspect Ratio Calculator. . . -s are too easy smh")
window.geometry("550x350")


math_label = Label(window, relief=RAISED, border=2, fg=text_color, bg=bg_again, font=("",45))
math_label.config(text=f"Meth:")
math_label.pack()

#frame
frame = Frame(window,bg=background_color)
frame.pack()

label = Label(frame,relief=RAISED,border=2,
              fg=text_color,bg=bg_again,
              text=f"Output!",font=("",30))
label.grid(row=1,column=1)

entry = Entry(frame,relief=RAISED,border=2,
              fg=entry_color,bg=entry_bg_color,width=8,font=("",30)
              )
entry.insert(0,1080)
entry.grid(row=1,column=0)
entry.bind("<Return>",math)

#
Label(frame,relief=RAISED,border=2,fg=text_color,bg=bg_again,text="Aspect 1:",font=("",30)).grid(row=2,column=0)
entryASP1 = Entry(frame,relief=RAISED,border=2,
                 fg=entry_color,bg=entry_bg_color,width=8,font=("",30)
                 )
entryASP1.grid(row=3,column=0)
entryASP1.insert(0,16)
entryASP1.bind("<Return>",change_asp)

#
Label(frame,relief=RAISED,border=2,fg=text_color,bg=bg_again,text="Aspect 2:",font=("",30)).grid(row=2,column=1)
entryASP2 = Entry(frame,relief=RAISED,border=2,
                 fg=entry_color,bg=entry_bg_color,width=8,font=("",30)
                 )
entryASP2.grid(row=3,column=1)
entryASP2.insert(0,9)
entryASP2.bind("<Return>",change_asp)


window.mainloop()

messagebox.showinfo(title="(not) IMPORTANT",message="people go to websites for this ez math smh")

if messagebox.askyesno(title="by the way-",message="Did you think you could close this without a virus?"):
    messagebox.showinfo(title="you're right",message="ok")
else:
    messagebox.showinfo(title="you're wrong",message="idk how to make a virus and if i did i wouldnt")
messagebox.showinfo(title="read me!",message="btw you should be reading the titles")
messagebox.showinfo(title="fun fact",message="did you see the top label saying meth instead of math when you first open it?")
messagebox.showinfo(title="to no suprise",message="i did")
if messagebox.askyesno(title="im tired",message="should i stop talking? i am kinda tired"):
    messagebox.showinfo(title="zzzZZZzzz",message="thanks")
else:
    messagebox.showinfo(title="*bedtime alarm noises*",message="too bad")
