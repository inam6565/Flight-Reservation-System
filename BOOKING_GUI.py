from tkinter import *
from tkinter import ttk
import sys
import ni3a

from datetime import date
import pandas as pd

import tkinter.messagebox

import v40


from v40 import bookflight
global dur,arrt,dept,ticketstatus




def fare_fun(a,classe):

    try:
        df1 = df[df['Flight'] == a]
        index = df1.index[df1['Flight'] == a].tolist()
        distance = df1['DISTANCE'][index[0]]
        if classe == "Business":
            if int(age_.get()) <= 3:
                return (distance*35)*(0.1)
            elif int(age_.get()) <= 12:
                return int((distance * 35) * 0.75)
            else:
                return distance*35

        elif classe == "A-Class":
            if int(age_.get()) <= 3:
                return (distance * 25) * (0.1)
            elif int(age_.get()) <= 12:
                return int((distance * 25) * 0.75)
            else:
                return distance * 25

        if classe == "Economy":
            if int(age_.get()) <= 3:
                return int((distance * 15) * 0.1)
            elif int(age_.get()) <= 12:
                return int((distance * 15) * 0.75)
            else:
                return distance * 15
    except:
        tkinter.messagebox.showerror("Error", "Please fill all the required fields !")




def book():
    global ldate, datelist, currentdate, name, lastname, email, namelist, lastnamelist, contact, contactlist, \
        emaillist
    global cnic, cniclist, gender, genderlist, seatno, seatnolist, tickets, totaltickets, ticketslist, price, \
        pricelist
    global age, agelist ,ticketclass,ticketclasslist,des,deslist,depc,depclist,dept,deptlist,arrc,arrclist,arrt,arrtlist
    global dur,durlist,ticketstatus

    name = name_.get()
    lastname = last_name_.get()
    cnic = cnic_.get()
    email = email_.get()
    contact = phone_.get()
    age = age_.get()
    gender = c5.get()
    des=des_comb.get()
    depc = from_comb.get()
    arrc = to_comb.get()
    ldate = date_comb.get()
    ticketclass= c9.get()
    flight = avail_comb.get()
    price = fare_fun(flight,ticketclass)



    if name=="" or last_name =="" or cnic ==0 or email=="" or contact ==0 or age ==0 or gender=="Select" or des=="Select" or \
            depc=="Select" or arrc=="Select" or ticketclass=="Select" or flight=="Select" :
        tkinter.messagebox.showerror("Error", "Please fill all the required fields !")

    else:
        MsgBox = tkinter.messagebox.askquestion ('','Are you sure you want to book this ticket',icon = 'warning')
        if MsgBox == 'yes':

            v40.name = name
            v40.lastname = lastname
            v40.cnic =int(cnic)
            v40.email = email
            v40.contact = int(contact)
            v40.age =int( age)
            v40.gender = gender
            v40.des = des
            v40.depc = depc
            v40.arrc = arrc
            v40.ldate = ldate
            v40.ticketclass = ticketclass
            v40.flight = flight
            v40.price = price
            v40.arrt=arrt
            v40.dept=dept
            v40.dur=dur
            v40.ticketstatus=ticketstatus

            v40.namelist.append(name)
            v40.lastnamelist.append(lastname)
            v40.cniclist.append(cnic)
            v40.emaillist.append(email)
            v40.contactlist.append(contact)
            v40.agelist.append(age)
            v40.genderlist.append(gender)

            v40.deslist.append(des)
            v40.depclist.append(depc)
            v40.arrclist.append(arrc)
            v40.datelist.append(ldate)

            v40.ticketclasslist.append(ticketclass)

            v40.flightlist.append(flight)

            v40.pricelist.append(price)

            v40.deptlist.append(dept)
            v40.arrtlist.append(arrt)
            v40.durlist.append(dur)

            bookflight()
            #time.sleep(2)


            tkinter.messagebox.showinfo('Return', 'You Ticket has been confirmed !')

            bookflight_window.destroy()




        else:
            tkinter.messagebox.showinfo('Return','You will now return to the Main Menu ')
            bookflight_window.destroy()






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


vframe=Frame(mainfame,bg="white")

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



#Top Status bar
status=Label(mainfame,text=" Book Flight",image=f112,compound=LEFT,bg="#ffffff",fg="#0c26af",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",18,"bold"))
status.pack(fill="x",side="top")



line1=Frame(vframe,bg="#f3f7f6")



name=Label(line1,text="Name : ",image=f113,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
name.grid(row=0,column=0,pady=10)
name_ = StringVar()
e1=Entry(line1,bg="#f3f7f6",fg="black",width=40,bd=0,textvariable=name_)
e1.grid(row=0,column=1,pady=10)



last_name=Label(line1,text="Last name : ",image=f113,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
last_name.grid(row=0,column=2,pady=10)
last_name_ = StringVar()
e2=Entry(line1,bg="#f3f7f6",fg="black",width=40,bd=0,textvariable=last_name_)
e2.grid(row=0,column=3,pady=10)



cnic=Label(line1,text="CNIC : ",image=f118,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=10)
cnic.grid(row=0,column=4,pady=10)
cnic_ = StringVar()
e6=Entry(line1,bg="#f3f7f6",fg="black",width=20,bd=0,textvariable=cnic_)
e6.grid(row=0,column=5)




line1.pack(side="top",fill="x",padx=10,pady=10)



#==------------------------------------------------------------------------------
line2=Frame(vframe,bg="#f3f7f6")


email=Label(line2,text="Email : ",image=f114,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
email.grid(row=0,column=0,pady=10)
email_ = StringVar()
e3=Entry(line2,bg="#f3f7f6",fg="black",width=40,bd=0,textvariable=email_)
e3.grid(row=0,column=1,pady=10)

phone=Label(line2,text="Phone number : ",image=f115,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
phone.grid(row=0,column=2,pady=5)
phone_=StringVar()
e4=Entry(line2,bg="#f3f7f6",fg="black",width=35,bd=0,textvariable=phone_)
e4.grid(row=0,column=3,pady=10)

age=Label(line2,text="Age :",image=f116,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
age.grid(row=0,column=4,pady=5)
age_ = StringVar()
e4=Entry(line2,bg="#f3f7f6",fg="black",width=20,bd=0,textvariable=age_)
e4.grid(row=0,column=5,pady=5)

gender=Label(line2,text="Gender : ",image=f117,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
gender.grid(row=0,column=6,pady=10)
fontc5 = ("Arial", 10)

c5=ttk.Combobox(line2,width=10,values=("Select","Male","Female","Other"),font=fontc5,state="readonly")

c5.grid(row=0,column=7,pady=10)
c5.current(0)



line2.pack(fill="x",padx=10,pady=10)




vframe.pack(fill="both",side="top",expand=1,padx=20,pady=20)


vframe2=Frame(mainfame,bg="white")

"""

cal1=Calendar(vframe2,selectmode="day",year=2021,month=3,day=10)

cal1.pack(side="right")
"""
#======================================================================================
line3=Frame(vframe2,bg="#f3f7f6")

#===using pandas here

df = pd.read_excel("inamdata1.xls")

classa = [
    "Select",
    "Economy",
    "A-Class",
    "Business",
]


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

def cloneseatgen():
    f = open("LIBRARIES\Seat_Generator.txt","rt")
    cloningsubject=f.read()
    f.close()
    f=open("LIBRARIES\Seat_Generator2.txt","wt")
    f.write(cloningsubject)
    f.close()



def detail_fun(e):
    global classa

    a = avail_comb.get()
    if a== "Select":
        return
    else:

        df1 = df[df['Flight'] == a]
        index=df1.index[df1['Flight'] == a].tolist()
        b = df1['DEPARTURE'][index[0]]
        c = df1['ARRIVAL'][index[0]]
        d = df1['Duration'][index[0]]

        global dept,arrt,dur,ticketstatus
        dept=b
        arrt=c
        dur=d

        dep_label.config(text=b)
        arr_label.config(text=c)
        dur_label.config(text=d)

        cloneseatgen()

        ni3a.ldate = date_comb.get()
        ni3a.ticketclass = c9.get()
        ni3a.flight = avail_comb.get()
        ni3a.seatno_gen()
        sumclasses = ni3a.sumclasses
        rseatno=ni3a.seatno
        eseats=ni3a.eseats
        aseats=ni3a.aseats
        bseats=ni3a.bseats


        if sumclasses ==200:
            tkinter.messagebox.showerror("Error", "No Tickets are available for this flight !")
            avail_comb.current(0)
            return

        if eseats==170:
            classa = [
                "Select",
                "A-Class",
                "Business",
            ]
            c9.config(state="readonly")

        elif aseats == 20:
            classa = [
                "Select",
                "Economy",
                "Business",
            ]
            c9.config(state="readonly")

        elif bseats == 10:
            classa = [
                "Select",
                "Economy",
                "A-Class",
            ]
            c9.config(state="readonly")

        elif aseats == 20 and bseats ==10:
             classa=["Select","Economy"]
        elif aseats == 20 and eseats ==170:
             classa=["Select","Business"]
        elif bseats == 10 and eseats ==170:
             classa=["Select","A-Class"]





        if sumclasses > 100:
            ticketstatus="Reserved"
            c9.config(state="readonly")
        else:
            ticketstatus="Booked"
            c9.config(state="readonly")


def avail_fun(e):
    avail_comb.config(values=[""])
    avail_comb.current(0)
    date_comb.config(state="readonly")


    global avail_list
    a = from_comb.get()
    b = to_comb.get()
    df1 = df[df['FROM'] == a]
    df2 = df1[df1['TO'] == b]
    avail_list = df2['Flight'].values.tolist()
    avail_comb.config(values=avail_list)


def pick(e):

    if des_comb.get() == "International":
        from_comb.config(state="readonly")

        to_comb.config(values=intl)

        from_comb.config(values=intl)
    if des_comb.get() == "Domestic":
        from_comb.config(state="readonly")

        to_comb.config(values=dom)
        from_comb.config(values=dom)

def pickoo(e):
    avail_comb.config(values=[""])
    avail_comb.current(0)
    to_comb.current(0)

    to_comb.config(state="readonly")


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

from_comb=ttk.Combobox(line3,width=30,values=["Select"],font=fontc5,state=DISABLED)
from_comb.grid(row=0,column=3,padx=10,pady=10)
from_comb.current(0)
from_comb.bind("<<ComboboxSelected>>", pickoo)




to=Label(line3,text="To : ",image=f120,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
to.grid(row=0,column=4,pady=10)

to_comb=ttk.Combobox(line3,width=35,values=["Select"],font=fontc5,state=DISABLED)
to_comb.grid(row=0,column=5,padx=20,pady=10)
to_comb.current(0)
to_comb.bind("<<ComboboxSelected>>", avail_fun)

def datoo(e):
    avail_comb.config(state="readonly")


"""
def cutoo():
    return
"""


line3.pack(fill="x",padx=10,pady=10)

#------------------------------------------------done

line4=Frame(vframe2,bg="#f3f7f6")

adate=Label(line4,text="Date : ",image=f122,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
adate.grid(row=0,column=0,pady=10)
ina = []

ina.append("Select")
today=date.today()
currentdate=today.day
for i in range(currentdate,32):
    w = str(i) + "/03/2021"
    ina.append(w)
date_comb=ttk.Combobox(line4,width=30,values=ina,font=fontc5,state=DISABLED)
date_comb.grid(row=0,column=1,padx=10,pady=10)
date_comb.current(0)
date_comb.bind("<<ComboboxSelected>>", datoo)



class_=Label(line4,text="Class: ",image=f123,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=10)
class_.grid(row=0,column=2,pady=10)

c9=ttk.Combobox(line4,width=30,values=classa,font=fontc5,state=DISABLED)
c9.grid(row=0,column=3,padx=10,pady=10)
c9.current(0)
#c9.bind("<<ComboboxSelected>>", cutoo)



avail=Label(line4,text="Available Flights : ",image=f124,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=10)
avail.grid(row=0,column=4,padx=5,pady=10)
avail_comb=ttk.Combobox(line4,width=27,values=["Select"],font=fontc5,state=DISABLED)
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
book_button=Button(line6,text="  Book  ",bg="#0c26af",fg="white",padx=5,pady=5,bd=0,command=book)
book_button.pack(pady=10,padx=5,side="right")
book_button.config(font=('Arial',10,'bold'))

cancel_button=Button(line6,text=" Back ",bg="#0c26af",fg="white",padx=5,pady=5,bd=0,command=bookflight_window.quit)
cancel_button.pack(pady=10,padx=5,side="right")
cancel_button.config(font=('Arial',10,'bold'))


line6.pack(fill="x",side="bottom",padx=10,pady=10)






vframe2.pack(fill="both",side="top",expand=1,padx=20,pady=20)


mainfame.pack(fill="both",side="top",expand=1)

bookflight_window.mainloop()