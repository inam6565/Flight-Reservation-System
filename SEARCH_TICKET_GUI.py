from tkinter import *
import re


from tkinter import messagebox

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
f128=PhotoImage(file ="images/AnyConv.com__boarding-pass2.gif")

f129=PhotoImage(file ="images/available1.gif")
f130=PhotoImage(file ="images/available3.gif")
f131=PhotoImage(file ="images/available2.gif")



#Top Status bar
status=Label(mainfame,text=" Search Ticket  ",image=f130,compound=LEFT,bg="#ffffff",fg="#0c26af",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",18,"bold"))
status.pack(fill="x",side="top")



def ticket_display(tkno):


    '''
    sta = "Ticket no." + str(tkno) + ".txt"
    a = subprocess.Popen(["notepad.exe", sta])
    returncode = a.wait()
    '''

    with open('LIBRARIES\Ticktets_data.txt', 'r') as datafile:
        entireDtaaText = datafile.read()
        datafile.seek(0, 0)
        ab = False
        for line_no in datafile:
            if tkno == int(line_no.split()[5]):
                ab = True
                resultl.config(text="Your Ticket has been found !")
                namelabel.config(text=line_no.split()[1])
                last_name_label.config(text=line_no.split()[2])
                cniclabel.config(text=line_no.split()[3])
                agel.config(text=line_no.split()[6])
                genderl.config(text=line_no.split()[7])
                seatno_label.config(text=line_no.split()[-1])
                bknolabel.config(text=line_no.split()[0])
                flight_label.config(text=line_no.split()[-2])
                datel.config(text=line_no.split()[16])
                pricel.config(text=line_no.split()[13])
                phnol.config(text=line_no.split()[5])
                emaill.config(text=line_no.split()[4])
                desl.config(text=line_no.split()[8])
                ticketclass_l.config(text=line_no.split()[14])
                froml.config(text=line_no.split()[9])
                tol.config(text=line_no.split()[10])
                deptl.config(text=line_no.split()[11])
                arrtl.config(text=line_no.split()[12])
                break
            else:
                ab = False
        if ab==True:
            return
        else:
            messagebox.showerror("Error", "No Match found .Please enter a valid CNIC number !")


def chk(k):
    global abc,tkno
    new = re.sub('[0-9]', '', k)
    try:
        if new.isalpha():
            messagebox.showerror("Error", "No Match found .Please enter a valid CNIC number !")
            ticketno_entry.delete(0,END)
            abc=False

        elif k == '':
            messagebox.showerror("Error", "No Match found .Please enter a valid CNIC number !")
            ticketno_entry.delete(0,END)
            abc=False
        else:
            tkno=int(k)
            return
    except:
        return
        return

def viewbookingdetails():
    global abc,tkno
    abc=True
    k = (ticketno_entry.get())

    chk(k)

    if abc==False:
        return
    else:
        f = open("LIBRARIES\Ticktets_Selector.txt")
        total_tickets=int(f.read())
        f.close()
        if tkno < 0:
            messagebox.showerror("Error", "No Match found .Please enter a valid CNIC number !")

        else:
            #print(tkno)
            ticket_display(tkno)











fontc5 = ("Arial", 10)

vframe2=Frame(mainfame,bg="white")

"""

cal1=Calendar(vframe2,selectmode="day",year=2021,month=3,day=10)

cal1.pack(side="right")
"""



#======================================================================================
line3=Frame(vframe2,bg="#0c26af")

ticketno=Label(line3,text="Enter your CNIC no : ",font=("Arial",14),image=f128,bg="#0c26af",compound=LEFT,fg="white",padx=10,pady=5)
ticketno.grid(row=0,column=0,pady=10)


ticketno_entry=Entry(line3,bg="#ffffff",width=60,font=("Arial",14),fg="#0c26af")
ticketno_entry.grid(row=0,column=1,pady=10)


book_button=Button(line3,text="  Search Booking Details  ",bg="#ffffff",fg="#0c26af",padx=5,pady=5,bd=0,command=viewbookingdetails)
book_button.grid(row=0,column=2,pady=10,padx=15)
book_button.config(font=('Arial',10,'bold'))

line3.pack(fill="x",padx=10,pady=5)

#------------------------------------------------done

line0=Frame(vframe2,bg="#ffffff")

fontc6 = ("Arial",14,"bold")

resultl=Label(line0,text="",bg="#ffffff",fg="#0c26af",padx=10,pady=5)
resultl.grid(row=0,column=0,pady=5,padx=20)



line0.pack(fill="x",padx=10,pady=5)




#===================================================
line4=Frame(vframe2,bg="#f3f7f6")

lname=Label(line4,text="Name : ",image=f113,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
lname.grid(row=0,column=0,pady=5)

namelabel=Label(line4,bg="#f3f7f6",fg="black",width=20,bd=0)
namelabel.grid(row=0,column=1,pady=5)



last_name=Label(line4,text="Last name : ",image=f113,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
last_name.grid(row=0,column=2,pady=10)
last_name_label=Label(line4,bg="#f3f7f6",fg="black",width=20,bd=0)
last_name_label.grid(row=0,column=3,pady=5)



lcnic=Label(line4,text="CNIC : ",image=f118,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lcnic.grid(row=0,column=4,pady=5)
cniclabel=Label(line4,bg="#f3f7f6",fg="black",width=20,bd=0)
cniclabel.grid(row=0,column=5,padx=15)



lage=Label(line4,text="Age : ",image=f116,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lage.grid(row=0,column=6,pady=5)
agel=Label(line4,bg="#f3f7f6",fg="black",width=20,bd=0)
agel.grid(row=0,column=7)


lgender=Label(line4,text="Gender : ",image=f117,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lgender.grid(row=0,column=8,pady=5)
genderl=Label(line4,bg="#f3f7f6",fg="black",width=20,bd=0)
genderl.grid(row=0,column=9)




line4.pack(fill="x",padx=10,pady=5)

#-----------------------------------------------------
line4a=Frame(vframe2,bg="#f3f7f6")


lname=Label(line4a,text="Booking No : ",image=f129,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
lname.grid(row=0,column=0,pady=5)

bknolabel=Label(line4a,bg="#f3f7f6",fg="black",width=15,bd=0)
bknolabel.grid(row=0,column=1,pady=5)



last_name=Label(line4a,text="Seat No : ",image=f129,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
last_name.grid(row=0,column=2,pady=10)
seatno_label=Label(line4a,bg="#f3f7f6",fg="black",width=22,bd=0)
seatno_label.grid(row=0,column=3,pady=5)



lcnic=Label(line4a,text="Flight : ",image=f124,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lcnic.grid(row=0,column=4,pady=5)
flight_label=Label(line4a,bg="#f3f7f6",fg="black",width=20,bd=0)
flight_label.grid(row=0,column=5,padx=10)



lage=Label(line4a,text="Date : ",image=f122,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lage.grid(row=0,column=6,pady=5,padx=10)
datel=Label(line4a,bg="#f3f7f6",fg="black",width=18,bd=0)
datel.grid(row=0,column=7)


lgender=Label(line4a,text="Price : ",image=f131,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lgender.grid(row=0,column=8,pady=5)
pricel=Label(line4a,bg="#f3f7f6",fg="black",width=20,bd=0)
pricel.grid(row=0,column=9)



line4a.pack(fill="x",padx=10,pady=5)
#-------------------------------------------------------done

#-----------------------------------------------------
line4b=Frame(vframe2,bg="#f3f7f6")


lname=Label(line4b,text="Phone No : ",image=f115,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
lname.grid(row=0,column=0,pady=5)

phnol=Label(line4b,bg="#f3f7f6",fg="black",width=16,bd=0)
phnol.grid(row=0,column=1,pady=5)



last_name=Label(line4b,text="Email : ",image=f114,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
last_name.grid(row=0,column=2,pady=10)
emaill=Label(line4b,bg="#f3f7f6",fg="black",width=24,bd=0)
emaill.grid(row=0,column=3,pady=5)



lcnic=Label(line4b,text="Destination : ",image=f119,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lcnic.grid(row=0,column=4,pady=5)
desl=Label(line4b,bg="#f3f7f6",fg="black",width=20,bd=0)
desl.grid(row=0,column=5)



lage=Label(line4b,text="TicketClass : ",image=f123,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lage.grid(row=0,column=6,pady=5)
ticketclass_l=Label(line4b,bg="#f3f7f6",fg="black",width=20,bd=0)
ticketclass_l.grid(row=0,column=7)




line4b.pack(fill="x",padx=10,pady=5)
#-------------------------------------------------------done


#-----------------------------------------------------
line4c=Frame(vframe2,bg="#f3f7f6")


lname=Label(line4c,text="From : ",image=f121,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
lname.grid(row=0,column=0,pady=5)

froml=Label(line4c,bg="#f3f7f6",fg="black",width=18,bd=0)
froml.grid(row=0,column=1,pady=5)



last_name=Label(line4c,text="To : ",image=f120,bg="#f3f7f6",compound=LEFT,fg="black",padx=10,pady=5)
last_name.grid(row=0,column=2,pady=10,padx=10)
tol=Label(line4c,bg="#f3f7f6",fg="black",width=24,bd=0)
tol.grid(row=0,column=3,pady=5)



lcnic=Label(line4c,text="Departure : ",image=f125,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lcnic.grid(row=0,column=4,pady=5,padx=6)
deptl=Label(line4c,bg="#f3f7f6",fg="black",width=20,bd=0)
deptl.grid(row=0,column=5,padx=2)



lage=Label(line4c,text="Arrival : ",image=f127,bg="#f3f7f6",compound=LEFT,fg="black",padx=5,pady=5)
lage.grid(row=0,column=6,pady=5)
arrtl=Label(line4c,bg="#f3f7f6",fg="black",width=20,bd=0)
arrtl.grid(row=0,column=7)



line4c.pack(fill="x",padx=10,pady=5)
#-------------------------------------------------------done





line4a.pack(fill="x",padx=10,pady=5)
#-------------------------------------------------------done



line6=Frame(vframe2,bg="#ffffff")

cancel_button=Button(line6,text=" Back ",bg="#0c26af",fg="white",padx=5,pady=5,bd=0,command=bookflight_window.destroy)
cancel_button.pack(pady=10,padx=5,side="right")
cancel_button.config(font=('Arial',10,'bold'))


line6.pack(fill="x",side="bottom",padx=10,pady=10)






vframe2.pack(fill="both",side="top",expand=1,padx=20,pady=20)


mainfame.pack(fill="both",side="top",expand=1)

bookflight_window.mainloop()