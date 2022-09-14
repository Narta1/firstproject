from ast import Lambda
from msilib import MSIMODIFY_INSERT_TEMPORARY
from telnetlib import STATUS
from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.geometry('500x900')
root.iconbitmap('icons8-invite-16.ico')

my_img=ImageTk.PhotoImage(Image.open('pic.jpg'))
my1=ImageTk.PhotoImage(Image.open('2.jpg'))
my2=ImageTk.PhotoImage(Image.open('3.jpg'))


lista=[my_img,my1,my2]
number=0
lbl=Label(image=my_img)
lbl.grid(row=0,column=0,columnspan=3)
status=Label(root,text="image 1 of "+ str(len(lista)),bd=1,fg="red",relief=SUNKEN,anchor=E)
status.grid(row=2,column=1,sticky=W+E)



def scrolling_next():
    global lbl
    global btn
    global btn2
    global number
    global status
    global current_index
    lbl.grid_forget
    number+=1
    
        


    if number<=len(lista)-1:




        lbl=Label(image=lista[number])
    
        lbl.grid(row=0,column=0,columnspan=3)
        
            
        btn=Button(root,text="Next", command=scrolling_next)
                
        btn.grid(row=1,column=2)
        btn2=Button(root,text='scroll previous',command=back)
        btn2.grid(row=1,column=0)
        status=Label(root,text="image "+str(number+1)+ "of "+ str(len(lista)),bd=1,fg="red",relief=SUNKEN,anchor=E)
        status.grid(row=2,column=1,sticky=W+E)
    else:
        root.destroy()

def back():
    global lbl
    global btn
    global btn2
    global number
    global status
    number-=1
    
    
    if   number>=0:
        lbl=Label(image=lista[number])
        lbl.grid(row=0,column=0,columnspan=3)
            
        btn=Button(root,text="Next", command=scrolling_next)
                
        btn.grid(row=1,column=2)
        btn2=Button(root,text='scroll previous',command=back)
        btn2.grid(row=1,column=0)
        status=Label(root,text="image "+str(number+1)+ "of "+ str(len(lista)),bd=1,fg="red",relief=SUNKEN,anchor=E)
        status.grid(row=2,column=1,sticky=W+E)
    else:
        root.destroy()


        



btn=Button(root,text="Next", command=scrolling_next)
btn.grid(row=1,column=2)
btn2=Button(root,text='scroll previous',command=back)
btn2.grid(row=1,column=0)


"""
btn=Button(root,text="quit",command=root.quit)
btn.pack()"""



root.mainloop()