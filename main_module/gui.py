import sys
from Tkinter import *
import tkMessageBox
import main


def call():
    int1=tkMessageBox.askokcancel("Confirmation","Do you want to generate questions")
    if int1:
        tkMessageBox.showwarning("Warning","Processing may take long time")
        int2=tkMessageBox.askokcancel("Confirmation","Do you want to continue")
    if int2:
       tkMessageBox.showinfo("Update","Your input text is processing.Wait for result")
       stx=en.get(1.0,END)
       list1=main.function(stx)
           
       root1=Tk()
         
       root1.config(bg='orange')
       root1.title("Generated Question")
       root1.minsize(width=1000, height=450)
       root1.maxsize(width=2000, height=666)



       options=("0","1","2","3","4","5","6","7","8","9")
       
       scrollbar = Scrollbar(root1)
       scrollbar.pack( side = RIGHT, fill=Y )
       k=1
       mylist = Listbox(root1, yscrollcommand = scrollbar.set,fg="black",font='5',bg='orange',height=666,width=2000)
       for i in range(len(list1)):
                if list1[i].startswith("Q.")==True:
                   mylist.insert(END,list1[i]+"      Question no.: "+str(k))
                   k=k+1
                else:
                    mylist.insert(END,list1[i])
       
       mylist.pack( side = LEFT,anchor=N)
       scrollbar.config( command = mylist.yview )
       #print mylist.size()
       if mylist.size()!=0:
          int3=tkMessageBox.askokcancel("Confirmation","Do you want to give rating")
          tkMessageBox.showinfo("Instruction","Enter question number using comma separater in appropiate rating box")
          tkMessageBox.showwarning("Warning","Every rating box should be initialized with zero")
          if int3:
              call4()
              
       root1.mainloop()
       

def call4():
    root3=Tk()
    root3.config(bg='green')
    root3.title("Rating submission")
    root3.minsize(width=600, height=600)
    root3.maxsize(width=750, height=750)

    
    l1=Label(root3,text="Rating 0:",font=1000,bg="orange",fg="brown")
    l1.place(relx=0.1,rely=0.01)

    en1=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en1.place(relx=0.3,rely=0.01)

    l2=Label(root3,text="Rating 1:",font=1000,bg="orange",fg="brown")
    l2.place(relx=0.1,rely=0.1)

    en2=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en2.place(relx=0.3,rely=0.1) 

    l3=Label(root3,text="Rating 2:",font=1000,bg="orange",fg="brown")
    l3.place(relx=0.1,rely=0.2)

    en3=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en3.place(relx=0.3,rely=0.2)

    l4=Label(root3,text="Rating 3:",font=1000,bg="orange",fg="brown")
    l4.place(relx=0.1,rely=0.3)

    en4=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en4.place(relx=0.3,rely=0.3) 

    l5=Label(root3,text="Rating 4:",font=1000,bg="orange",fg="brown")
    l5.place(relx=0.1,rely=0.4)

    en5=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en5.place(relx=0.3,rely=0.4) 

    l6=Label(root3,text="Rating 5:",font=1000,bg="orange",fg="brown")
    l6.place(relx=0.1,rely=0.5)

    en6=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en6.place(relx=0.3,rely=0.5)

    l7=Label(root3,text="Rating 6:",font=1000,bg="orange",fg="brown")
    l7.place(relx=0.1,rely=0.6)

    en7=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en7.place(relx=0.3,rely=0.6)

    l8=Label(root3,text="Rating 7:",font=1000,bg="orange",fg="brown")
    l8.place(relx=0.1,rely=0.7)

    en8=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en8.place(relx=0.3,rely=0.7)

    l9=Label(root3,text="Rating 8:",font=1000,bg="orange",fg="brown")
    l9.place(relx=0.1,rely=0.8)

    en9=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en9.place(relx=0.3,rely=0.8)

    l10=Label(root3,text="Rating 9:",font=1000,bg="orange",fg="brown")
    l10.place(relx=0.1,rely=0.9)

    en10=Text(root3,bg="pink",bd=5,fg="black",width=50,height=1)
    en10.place(relx=0.3,rely=0.9) 
    
    btx=Button(root3,text="submit",command=lambda:call5(en1,en2,en3,en4,en5,en6,en7,en8,en9,en10),relief=RAISED,padx=5,pady=5,bd=5,bg="orange",fg="cyan",activebackground="red",cursor="spider")
    btx.place(relx=0.28,rely=0.95)
    btx.flash()    
           
    root3.mainloop()


def call5(en1,en2,en3,en4,en5,en6,en7,en8,en9,en10):

    int7=tkMessageBox.askokcancel("Confirmation","Do you want submit your rating finally")

    if int7:    
       root4=Tk()
       root4.config(bg='cyan')
       root4.title("Your judgement report")
       root4.minsize(width=400, height=400)
       root4.maxsize(width=450, height=450)
    #en1.insert(1.0,'0,')


       fo=open("Report.txt","a+")
       fo.write("----------------------------------\n")    

       listx=str(en1.get(1.0,END)).split(",")
       m=len(listx)
 
       fo.write("Rating  0: "+str(m-1)+"\n")
  
       l1=Label(root4,text="Rating 0:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l1.place(relx=0.1,rely=0.01)
   # en2.insert(1.0,'0,')
   
       listx=str(en2.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  1: "+str(m-1)+"\n")

       l2=Label(root4,text="Rating 1:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l2.place(relx=0.1,rely=0.1)
    #en3.insert(1.0,'0,')
    
       listx=str(en3.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  2: "+str(m-1)+"\n")

       l3=Label(root4,text="Rating 2:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l3.place(relx=0.1,rely=0.2)
    #en4.insert(1.0,'0,')
    
       listx=str(en4.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  3: "+str(m-1)+"\n")
    
       l4=Label(root4,text="Rating 3:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l4.place(relx=0.1,rely=0.3)
    #en5.insert(1.0,'0,')
    
       listx=str(en5.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  4: "+str(m-1)+"\n")

       l5=Label(root4,text="Rating 4:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l5.place(relx=0.1,rely=0.4)
    #en6.insert(1.0,'0,')
    
       listx=str(en6.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  5: "+str(m-1)+"\n")

       l6=Label(root4,text="Rating 5:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l6.place(relx=0.1,rely=0.5)
    #en7.insert(1.0,'0,')
    
       listx=str(en7.get(1.0,END)).split(",")
       m=len(listx)

       fo.write("Rating  6: "+str(m-1)+"\n")

       l7=Label(root4,text="Rating 6:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l7.place(relx=0.1,rely=0.6)
    #en8.insert(1.0,'0,')
    
       listx=str(en8.get(1.0,END)).split(",")
       m=len(listx) 

       fo.write("Rating  7: "+str(m-1)+"\n")
      
       l8=Label(root4,text="Rating 7:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l8.place(relx=0.1,rely=0.7)
    #en9.insert(1.0,'0,')
    
       listx=str(en9.get(1.0,END)).split(",")
       m=len(listx) 

       fo.write("Rating  8: "+str(m-1)+"\n")
      
       l9=Label(root4,text="Rating 8:    "+str(m-1),font=1000,bg="cyan",fg="brown")
       l9.place(relx=0.1,rely=0.8)
    #en10.insert(1.0,'0,')
    
       listx=str(en10.get(1.0,END)).split(",")
       m=len(listx) 

       fo.write("Rating  9: "+str(m-1)+"\n")
   
       l10=Label(root4,text="Rating 9:   "+str(m-1),font=1000,bg="cyan",fg="brown")
       l10.place(relx=0.1,rely=0.9)

       fo.close() 

       root4.mainloop()
              

def call1():
    en.delete(1.0,END)

def call2():
    root.destroy()   
    
root=Tk()
root.config(bg="orange")
root.title("NATURAL  LANGUAGE  QUESTION  GENERATION ")
root.minsize(width=600, height=600)
root.maxsize(width=750, height=750)
frame=Frame(root)
frame.place(relx=0.3,rely=0.25)



lb1=Label(root,text="ENTER  TEXT",font=1000,bg="orange",fg="brown")
lb1.place(relx=0.1,rely=0.3)


en=Text(root,bg="pink",bd=5,fg="black",height=5,width=50)
en.place(relx=0.3,rely=0.3)

var=StringVar()

bt=Button(root,text="OK",command=call,relief=RAISED,padx=8,pady=8,bd=8,bg="black",fg="orange",activebackground="red",cursor="spider")
bt.place(relx=0.38,rely=0.5)
bt.flash()

bt1=Button(root,text="RESET",relief=RAISED,command=call1,padx=8,pady=8,bd=8,bg="black",fg="orange",activebackground="red",cursor="spider")
bt1.place(relx=0.5,rely=0.5)
bt1.flash()

bt2=Button(root,text="EXIT",relief=RAISED,command=call2,padx=8,pady=8,bd=8,bg="black",fg="orange",activebackground="red",cursor="spider")
bt2.place(relx=0.65,rely=0.5)
bt2.flash()

    
root.mainloop()

    
    
