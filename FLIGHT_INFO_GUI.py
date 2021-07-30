from tkinter import *
from tkinter import ttk
import pandas as pd

#from tkcalendar import Calendar




bookflight_window=Tk()

bookflight_window.title(
    "Flight Reservation system            Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar DSA CEP BEE 56 D")
bookflight_window.iconbitmap('images/icon1.ico')
bookflight_window.geometry('1500x700')
#Bottom Status bar
status1=Label(text="Copyrights © 2021.Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar . All Copyrights reserved.",bg="white",fg="#0c26af",bd=10,relief=FLAT,anchor=W)
status1.config(font=("Arial",10,"bold"))
status1.pack(fill="x",side="bottom")


mainfame=Frame(bookflight_window,bg="#0c26af")



f112=PhotoImage(file ="images/fi-rr-align-justify_blue.gif")
f113=PhotoImage(file ="images/fi-rr-user.gif")
f114=PhotoImage(file ="images/fi-rr-envelope.gif")
f115=PhotoImage(file ="images/phone1.gif")
f116=PhotoImage(file ="images/fi-rr-user-time.gif")
f117=PhotoImage(file ="images/toilet-signs.gif")
f118=PhotoImage(file ="images/fi-rr-id-badge.gif")



f119=PhotoImage(file ="images/destination3.gif")
f120=PhotoImage(file ="images/to1.gif")
f121=PhotoImage(file ="images/from1.gif")
f122=PhotoImage(file ="images/datea1.gif")
f123=PhotoImage(file ="images/ticketclass.gif")
f124=PhotoImage(file ="images/available4.gif")

f125=PhotoImage(file ="images/AnyConv.com__012-time.gif")
f126=PhotoImage(file ="images/AnyConv.com__002-flag.gif")
f127=PhotoImage(file ="images/AnyConv.com__013-clock-1.gif")

f128=PhotoImage(file ="images/AnyConv.com__ARY_banner2.gif")


#Top Status bar
status=Label(mainfame,text=" Flight Information",image=f112,compound=LEFT,bg="white",fg="#0c26af",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",18,"bold"))
status.pack(fill="x",side="top")

list_flights = []
df = pd.read_excel("inamdata1.xls")

def info():
    a = mylist.get(ANCHOR)
    df1 = df[df["Flight"] == a]
    index = df1.index[df1['Flight'] == a].tolist()
    e = df1['TO'][index[0]]
    f = df1['FROM'][index[0]]
    b = df1['DEPARTURE'][index[0]]
    c = df1['ARRIVAL'][index[0]]
    d = df1['Duration'][index[0]]
    from2.config(text=f)
    to2.config(text=e)
    dep2.config(text=b)
    arr2.config(text=c)
    dur2.config(text=d)
def pick(e):
    global list_flights
    a = c6.get()
    df1 = df[df['Destination'] == a]
    list_flights = df1['Flight'].values.tolist()
    if a == "International":
        s1=32
    if a == "Select":
        return


    elif a == "Domestic":
        s1 = 24


    mylist.delete(0,END)
    for i in range (s1):
        mylist.insert(END,list_flights[i])



vframe2=Frame(mainfame,bg="#0c26af")


# Header logo
logoframe = Frame(vframe2, bg="white", relief=FLAT, bd=0)
logoframe.pack(side="top", fill="x",padx=10)

logo1 = Label(logoframe, image=f128,bg="#15327c", relief=FLAT, bd=0)
logo1.pack(side="top",fill="x")

#-----------------------------------------------------------------------------------
vframe2a=Frame(vframe2,bg="white",bd=0)

line1=Frame(vframe2a,bg="#f3f7f6",bd=0)

l7=Label(line1,text="Destination : ",image=f119,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
l7.grid(row=0,column=0,pady=10)
destination =[
    "Select",
    "International",
    "Domestic",
]
c6=ttk.Combobox(line1,width=30,values=destination,font=("Arial",10,"bold"),state="readonly")
c6.grid(row=0,column=1,pady=10)
c6.current(0)
c6.bind("<<ComboboxSelected>>", pick)
line1.pack(side="top",padx=5,pady=5,fill="x")

line2=Frame(vframe2a,bg="#ffffff",bd=0)

scrollbar = Scrollbar(vframe2a)
scrollbar.pack( side =RIGHT, fill = Y )
mylist = Listbox(line2, width=50,yscrollcommand = scrollbar.set )


mylist.pack( side = LEFT, fill = BOTH ,padx=10,pady=5)
scrollbar.config( command = mylist.yview )

#------------------------------------------------------------------------

line3=Frame(vframe2a,bg="#ffffff",bd=0)

detail_button=Button(line3,text="Flight Information",bg="#0c26af",fg="white",bd=0,padx=20,pady=10,command=info)
detail_button.pack(side="right",padx=10,pady=10)
line3.pack(side="bottom",padx=25,pady=5,fill="x")

#------------------------------------------------------------------------

line2.pack(side="top",padx=5,pady=5,fill="both",expand=1)

vframe2a.pack(fill="both",side="left",padx=10,expand=1,pady=20)
#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
vframe2b=Frame(vframe2,bg="white",bd=0)


#------------------------------------------------------------------------

line41=Frame(vframe2b,bg="#f3f7f6",bd=0)

from1=Label(line41,text="From :                 ",bg="#f3f7f6",image=f120,compound=LEFT,fg="black",bd=0,padx=10,pady=10)
from1.grid(row=0,column=0,pady=5)


from2=Label(line41,text="",bg="#f3f7f6",width=100,fg="black",bd=0,padx=10,pady=10)
from2.grid(row=0,column=1,pady=5)

line41.pack(side="top",padx=10,pady=5,fill="x")

#------------------------------------------------------------------------
#------------------------------------------------------------------------

line42=Frame(vframe2b,bg="#f3f7f6",bd=0)


to1=Label(line42,text="To :                      ",bg="#f3f7f6",image=f121,compound=LEFT,fg="black",bd=0,padx=10,pady=10)
to1.grid(row=0,column=0,pady=5)


to2=Label(line42,text="",bg="#f3f7f6",width=100,fg="black",bd=0,padx=10,pady=10)
to2.grid(row=0,column=1,pady=5)


line42.pack(side="top",padx=10,pady=5,fill="x")

#------------------------------------------------------------------------


#------------------------------------------------------------------------

line43=Frame(vframe2b,bg="#f3f7f6",bd=0)


dep1=Label(line43,text="Departure time :",bg="#f3f7f6",image=f125,compound=LEFT,fg="black",bd=0,padx=10,pady=10)
dep1.grid(row=0,column=0,pady=5)


dep2=Label(line43,text="",bg="#f3f7f6",width=100,fg="black",bd=0,padx=10,pady=10)
dep2.grid(row=0,column=1,pady=5)

line43.pack(side="top",padx=10,pady=5,fill="x")

#------------------------------------------------------------------------


#------------------------------------------------------------------------

line44=Frame(vframe2b,bg="#f3f7f6",bd=0)

arr1=Label(line44,text="Arrival time :      ",bg="#f3f7f6",image=f126,compound=LEFT,fg="black",bd=0,padx=10,pady=10)
arr1.grid(row=0,column=0,pady=5)


arr2=Label(line44,text="",bg="#f3f7f6",width=100,fg="black",bd=0,padx=10,pady=10)
arr2.grid(row=0,column=1,pady=5)


line44.pack(side="top",padx=10,pady=5,fill="x")

#------------------------------------------------------------------------


#------------------------------------------------------------------------

line45=Frame(vframe2b,bg="#f3f7f6",bd=0)

dur1=Label(line45,text="Duration :       ",bg="#f3f7f6",image=f127,compound=LEFT,fg="black",bd=0,padx=10,pady=10)
dur1.grid(row=0,column=0,pady=5)


dur2=Label(line45,text="",bg="#f3f7f6",width=100,fg="black",bd=0,padx=10,pady=10)
dur2.grid(row=0,column=1,pady=5,padx=6)


line45.pack(side="top",padx=10,pady=5,fill="x")

#------------------------------------------------------------------------


vframe2b.pack(fill="both",side="right",expand=1,padx=10,pady=20)
#-----------------------------------------------------------------------------------



vframe2.pack(fill="both",side="top",expand=1,padx=20,pady=20)

#-----------------------------------------------------------------------------------

mainfame.pack(fill="both",side="top",expand=1)

bookflight_window.mainloop()