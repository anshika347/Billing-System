from tkinter import *
root = Tk()
root.title("BILLING management system")
root.geometry('1280x720')
bg_color='brown'
title=Label(root,text='Billing  system ',bg=bg_color,fg='white',font=('times new roman',25,'bold'))
title.pack(fill=X) 
#product details
F1=LabelFrame(root,text='productdetails', font=('times new roman',15,'bold'),fg='gold')
F1.place(x=5,y=90,width=800,height=500)
#heading
itm=Label(F1,text='Items',font=('Helvatic',25,'bold'),fg='black')
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='number of items',font=('Helvatic',25,'bold'),fg='black')
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='cost of items',font=('Helvatic',25,'bold'),fg='black')
cost.grid(row=0,column=2,padx=20,pady=15)
#product
bread=Label(F1,text='bread',font=('times new roman',20,'bold'),fg='lawngreen')
bread.grid(row=1,column=0,padx=20,pady=15)

b_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
b_txt.grid(row=1,column=1,padx=20,pady=15)

c_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
c_txt.grid(row=1,column=2,padx=20,pady=15)

egg=Label(F1,text='egg',font=('times new roman',20,'bold'),fg='lawngreen')
egg.grid(row=2,column=0,padx=20,pady=15)

egg_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
egg_txt.grid(row=2,column=1,padx=20,pady=15)

egg_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
egg_txt.grid(row=2,column=2,padx=20,pady=15)

total=Label(F1,text='Total',font=('times new roman',20,'bold'),fg='lawngreen')
total.grid(row=3,column=0,padx=20,pady=15)

total_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
total_txt.grid(row=3,column=1,padx=20,pady=15)

total_txt=Entry(F1,font='aerial 15 bold',relief=SUNKEN,bd=7,justify=CENTER)
total_txt.grid(row=3,column=2,padx=20,pady=15)

#----------BILING AREA---------------------------

F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='recipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
#add a scrollbar.
textarea=Text(F2,font='arial 15 bold')

textarea.pack(fill=BOTH)


#---------BUTTON--------------
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=5,y=590,width=1270,height=120)

btn1=Button(F3,text='total',font='arial 25 bold',bg='yellow',fg='crimson')
btn1.grid(row=0,column=0,pady=10)
root.mainloop()


