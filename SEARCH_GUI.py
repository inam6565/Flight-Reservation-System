from tkinter import *
from tkinter import ttk
import pandas as pd
import os
from datetime import date
#from tkcalendar import Calendar




bookflight_window=Tk()

bookflight_window.title(
    "Flight Reservation system            Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar DSA CEP BEE 56 D")
bookflight_window.iconbitmap('images/icon1.ico')
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
f129=PhotoImage(file ="images/available1.gif")
f130=PhotoImage(file ="images/available3.gif")


#Top Status bar
status=Label(mainfame,text=" Search Flight",image=f112,compound=LEFT,bg="#ffffff",fg="#0c26af",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",18,"bold"))
status.pack(fill="x",side="top")









vframe2=Frame(mainfame,bg="white")


# Header logo
logoframe = Frame(vframe2, bg="#ffffff", relief=FLAT, bd=0)
logoframe.pack(side="top", fill="x")

logo1 = Label(logoframe, image=f128,bg="#15327c", relief=FLAT, bd=0)
logo1.pack(side="top",fill="x")



"""

cal1=Calendar(vframe2,selectmode="day",year=2021,month=3,day=10)

cal1.pack(side="right")
"""
#======================================================================================
line3=Frame(vframe2,bg="#f3f7f6")

#===using pandas here

df = pd.read_excel("inamdata1.xls")

intl = [
        "Select",
        "Karachi",
        "Lahore",
        "Toronto",
        "Beijing",
        "Medina",
        "London",
]
dom =[
            "Select",
            "Islamabad",
            "Karachi",
            "Lahore",
            "Skardu",
        ]
avail_list = []

def detail_fun(e):
    a = avail_comb.get()

    df1 = df[df['Flight'] == a]
    index=df1.index[df1['Flight'] == a].tolist()
    b = df1['DEPARTURE'][index[0]]
    c = df1['ARRIVAL'][index[0]]
    d = df1['Duration'][index[0]]
    dep_label.config(text=b)
    arr_label.config(text=c)
    dur_label.config(text=d)

def avail_fun(e):
    avail_comb.config(values=[""])
    avail_comb.current(0)

    global avail_list
    a = from_comb.get()
    b = to_comb.get()
    df1 = df[df['FROM'] == a]
    df2 = df1[df1['TO'] == b]
    avail_list = df2['Flight'].values.tolist()
    avail_comb.config(values=avail_list)



def pickoo(e):
    avail_comb.config(values=[""])
    avail_comb.current(0)
    to_comb.current(0)



def pick(e):
    if des_comb.get() == "International":
        to_comb.config(values=intl)
        from_comb.config(values=intl)
    if des_comb.get() == "Domestic":
        to_comb.config(values=dom)
        from_comb.config(values=dom)

fontc5 = ("Arial", 10)

des=Label(line3,text="Destination : ",image=f119,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
des.grid(row=0,column=0,pady=10)
destination =[
    "Select",
    "International",
    "Domestic",
]
des_comb=ttk.Combobox(line3,width=26,values=destination,font=fontc5,state="readonly")
des_comb.grid(row=0,column=1,pady=10)
des_comb.current(0)
des_comb.bind("<<ComboboxSelected>>", pick)


from_=Label(line3,text="From: ",image=f121,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
from_.grid(row=0,column=2,pady=10,padx=5)

from_comb=ttk.Combobox(line3,width=30,values=["Select"],font=fontc5,state="readonly")
from_comb.grid(row=0,column=3,padx=10,pady=10)
from_comb.current(0)
from_comb.bind("<<ComboboxSelected>>", pickoo)



to=Label(line3,text="To : ",image=f120,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
to.grid(row=0,column=4,pady=10)

to_comb=ttk.Combobox(line3,width=35,values=["Select"],font=fontc5,state="readonly")
to_comb.grid(row=0,column=5,padx=20,pady=10)
to_comb.current(0)
to_comb.bind("<<ComboboxSelected>>", avail_fun)









line3.pack(fill="x",padx=10,pady=10)

#------------------------------------------------done

line4=Frame(vframe2,bg="#f3f7f6")

datel=Label(line4,text="Date : ",image=f122,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
datel.grid(row=0,column=0,pady=10)
ina = []

ina.append("Select")
today=date.today()
currentdate=today.day
for i in range(currentdate,32):
    w = str(i) + "/03/2021"
    ina.append(w)
date_comb=ttk.Combobox(line4,width=30,values=ina,font=fontc5,state="readonly")
date_comb.grid(row=0,column=1,padx=10,pady=10)
date_comb.current(0)



avail=Label(line4,text="Available Flights : ",image=f124,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=10)
avail.grid(row=0,column=4,padx=5,pady=10)
avail_comb=ttk.Combobox(line4,width=27,values=["Select"],font=fontc5,state="readonly")
avail_comb.grid(row=0,column=5,padx=10,pady=10)
avail_comb.current(0)
avail_comb.bind("<<ComboboxSelected>>", detail_fun)




line4.pack(fill="x",padx=10,pady=10)
#-------------------------------------------------------done
line5=Frame(vframe2,bg="#f3f7f6")
dep_time=Label(line5,text="Departure time : ",image=f125,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
dep_time.grid(row=0,column=0,pady=10)

dep_label=Label(line5,bg="#f3f7f6",fg="black",width=28,bd=0)
dep_label.grid(row=0,column=1,pady=10)

arr_time=Label(line5,text="Arrival time : ",image=f126,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
arr_time.grid(row=0,column=2,pady=10)

arr_label=Label(line5,bg="#f3f7f6",fg="black",width=31,bd=0)
arr_label.grid(row=0,column=3,pady=10)

duration=Label(line5,text="Duration : ",image=f127,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=10)
duration.grid(row=0,column=4,pady=10,padx=10)

dur_label=Label(line5,bg="#f3f7f6",fg="black",width=5,bd=0)
dur_label.grid(row=0,column=5)

line5.pack(fill="x",padx=10,pady=10)

#==========----------------------====================-------------====================-----------------

line6=Frame(vframe2,bg="#ffffff")


cancel_button=Button(line6,text=" Back ",bg="#0c26af",fg="white",padx=5,pady=5,bd=0,command=bookflight_window.destroy)
cancel_button.pack(pady=10,padx=5,side="right")
cancel_button.config(font=('Arial',10,'bold'))


line6.pack(fill="x",side="bottom",padx=10,pady=10)






vframe2.pack(fill="both",side="top",expand=1,padx=20,pady=20)


mainfame.pack(fill="both",side="top",expand=1)

bookflight_window.mainloop()