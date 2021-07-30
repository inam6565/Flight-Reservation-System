from tkinter import *
import re
import os
import ni3b
from tkinter import messagebox
from datetime import date
triprefund=0

bookflight_window = Tk()
bookflight_window.title(
    "Flight Reservation system            Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar DSA CEP BEE 56 D")
bookflight_window.iconbitmap('images/icon1.ico')

# Bottom Status bar
status1 = Label(
    text="Copyrights © 2021.Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar . All Copyrights reserved.",
    bg="white", fg="#0c26af", bd=10, relief=FLAT, anchor=W)
status1.config(font=("Arial", 10, "bold"))
status1.pack(fill="x", side="bottom")

mainfame = Frame(bookflight_window, bg="#0c26af")

f112 = PhotoImage(file="images/fi-rr-align-justify_blue.gif")
f113 = PhotoImage(file="images/fi-rr-user.gif")
f114 = PhotoImage(file="images/fi-rr-envelope.gif")
f115 = PhotoImage(file="images/phone1.gif")
f116 = PhotoImage(file="images/fi-rr-user-time.gif")
f117 = PhotoImage(file="images/toilet-signs.gif")
f118 = PhotoImage(file="images/fi-rr-id-badge.gif")

f119 = PhotoImage(file="images/destination3.gif")
f120 = PhotoImage(file="images/to1.gif")
f121 = PhotoImage(file="images/from1.gif")
f122 = PhotoImage(file="images/datea1.gif")
f123 = PhotoImage(file="images/ticketclass.gif")
f124 = PhotoImage(file="images/available4.gif")

f125 = PhotoImage(file="images/AnyConv.com__012-time.gif")
f126 = PhotoImage(file="images/AnyConv.com__002-flag.gif")
f127 = PhotoImage(file="images/AnyConv.com__013-clock-1.gif")
f128 = PhotoImage(file="images/AnyConv.com__boarding-pass2.gif")

# Top Status bar
status = Label(mainfame, text=" Cancel Trip ", image=f112, compound=LEFT, bg="#ffffff", fg="#0c26af", bd=10,
               relief=FLAT, anchor=W)
status.config(font=("Arial", 18, "bold"))
status.pack(fill="x", side="top")


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

def trip_display(trpno):
    global triprefund

    with open('LIBRARIES\Trip_data.txt', 'r') as datafile:
        #print("trip")
        entireDtaaText = datafile.read()
        datafile.seek(0, 0)
        abe = False
        #print("trip display3")
        for line_no in datafile:
            #print("trip display4")

            if str(trpno) == line_no.split()[0]:
                #print("trip found")
                abe=True
                tickets=line_no.split()[1]
                firstticket=line_no.split()[2]

                tripline=line_no

            else:
                abe = False
        if abe == True:
            #print("true")

            for i in range(int(tickets)):
                #print("loop")
                cancelticketdetails(int(firstticket)+i)

            #print("deleted tickets")

            with open("LIBRARIES\Trip_data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if tripline not in line:
                        f.write(line)
                f.truncate()

            messagestr = "Your Refund is Rs. " + str(int(triprefund))

            messagebox.showinfo("Cancel Flight", messagestr)
            bookflight_window.destroy()




        else:
            messagebox.showerror("Error", "No Match found .Please enter a valid Ticket number !")
    return
#-------------------------------------------------------------------------------------------



def trpchk(k):
    global abcd, trpno
    new = re.sub('[0-9]', '', k)
    try:
        if new.isalpha():
            messagebox.showerror("Error", "No Match found .Please enter a valid Ticket number !")
            ticketno_entry.delete(0, END)
            abcd = False

        elif k == '':
            messagebox.showerror("Error", "No Match found .Please enter a valid Ticket number !")
            ticketno_entry.delete(0, END)
            abcd = False
        else:
            trpno = int(k)
            return
    except:
        return


def canceltripdetails():
    #print("1")
    global abcd, trpno
    abcd = True
    t = (ticketno_entry.get())
    #print("2")

    trpchk(t)
    #print(trpno)
    #print("3")
    try:
        #print("4")

        if abcd == False:
            #print("4")
            return
        else:
            #print("5")
            f = open("LIBRARIES\Trip_Selector.txt")
            totaltrips = int(f.read())
            #print(totaltrips)
            f.close()

            if trpno < 0:
                messagebox.showerror("Error", "No Match found .Please enter a valid Trip number !")
            elif trpno > totaltrips:
                messagebox.showerror("Error", "No Match found .Please enter a valid Trip number !")

            else:
                #print(trpno)
                #print("3")
                trip_display(trpno)


    except:

        return


#--------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

def updatereserves(seatno):
    with open("LIBRARIES\Res_data.txt", "r") as file:
        first_line = file.readline()
        key = int(first_line)

        with open('LIBRARIES\Ticktets_data.txt', 'r') as datafile:
            entireDtaaText = datafile.read()
            datafile.seek(0, 0)
            ab = False
            for line_no in datafile:
                if key == int(line_no.split()[0]):
                    ab = True
                    # resultl.config(text="Your Ticket has been found !")
                    line_no.split()[-1] = seatno
                    break
                else:
                    ab = False
            if ab == True:
                f = open("LIBRARIES\Res_Selector.txt", "rt")
                reservetickets = int(f.read()) - 1
                f.close()
                f = open("LIBRARIES\Res_Selector.txt", "rt")
                f.write(str(reservetickets))
                f.close()

                with open("LIBRARIES\Ticktets_data.txt", "r") as f:
                    lines = f.readlines()
                with open("LIBRARIES\Ticktets_data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != str(key):
                            f.write(line)

                return
            else:
                f = open("LIBRARIES\Res_Selector.txt", "rt")
                reservetickets = int(f.read()) - 1
                f.close()
                f = open("LIBRARIES\Res_Selector.txt", "rt")
                f.write(str(reservetickets))
                f.close()

                with open("LIBRARIES\Ticktets_data.txt", "r") as f:
                    lines = f.readlines()
                with open("LIBRARIES\Ticktets_data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != str(key):
                            f.write(line)
                return




def ticket_display(tkno):
    global triprefund
    #print("ticket display1")
    with open('LIBRARIES\Ticktets_data.txt', 'r') as datafile:
        #print("ticket display2")

        entireDtaaText = datafile.read()
        datafile.seek(0, 0)
        ab = False
        #print("ticket display3")

        for line_no in datafile:
            #print("ticket display4")

            if str(tkno) == line_no.split()[0]:
                #print("ticket display5")

                refund = int(line_no.split()[-6])
                flight = line_no.split()[-2]
                del_dateb = line_no.split()[-3]
                del_date = del_dateb.split("/")[0]
                ticketclass = line_no.split()[-5]

                ni3b.flight = flight
                ni3b.ldate = del_dateb
                ni3b.ticketclass = ticketclass
                #print("ticket display6")

                ni3b.seatno_gen()
                #print("Seatno_gen completed found !")

                today = date.today()
                current_date = int(today.day)
                #print("ticket display today date ", current_date)

                seatno = line_no.split()[-1]
                f = open("LIBRARIES\Res_Selector.txt", "rt")
                reservetickets = int(f.read())
                f.close()
                if reservetickets > 0:
                    #print("There is a reserve ticket going to update reserves")
                    updatereserves(seatno)

                dif = int(del_date) - current_date
                #print("ticket display date diff")

                if dif >= 3:
                    refund = int(refund) * 0.75
                    #print("refund 75%")
                elif dif == 2:
                    refund = int(refund) * 0.50
                    #print("refund 50%")

                elif dif == 1:
                    refund = int(refund) * 0.25
                    #print("refund 25%")

                else:
                    refund = 0
                    #print("refund 0%")

                triprefund=triprefund+refund


                ab = True
                cd = line_no
                #print(cd)

                break
            else:
                ab = False
        if ab == True:

            with open("LIBRARIES\Ticktets_data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if cd not in line:
                        f.write(line)
                f.truncate()
            """
            with open("LIBRARIES\Ticktets_data.txt", "r") as f:
                lines = f.readlines()
            with open("LIBRARIES\Ticktets_data.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != cd:
                        f.write(line)

            """

            filename = "Ticket no." + str(tkno) + ".txt"
            #print(filename)
            os.remove(filename)

            return
        else:
            return


def cancelticketdetails(k):
    #print("agaya")

    global abc, tkno
    abc = True
    #print('In')
    tkno=k


    #print(tkno)
    #print("ffffff")
    try:

        if abc == False:
            return
        else:
            f = open("LIBRARIES\Ticktets_Selector.txt")
            total_tickets = int(f.read())
            f.close()
            if tkno < 0:
                messagebox.showerror("Error", "No Match found .Please enter a valid Ticket number !")
            elif tkno > total_tickets:
                messagebox.showerror("Error", "No Match found .Please enter a valid Ticket number !")
            else:
                #print(tkno)
                ticket_display(tkno)

    except:
        return


fontc5 = ("Arial", 10)

vframe2 = Frame(mainfame, bg="white")

"""

cal1=Calendar(vframe2,selectmode="day",year=2021,month=3,day=10)

cal1.pack(side="right")
"""

# ======================================================================================
line3 = Frame(vframe2, bg="#0c26af")

ticketno = Label(line3, text="Enter your Trip no : ", font=("Arial", 14), image=f128, bg="#0c26af", compound=LEFT,
                 fg="white", padx=10, pady=5)
ticketno.grid(row=0, column=0, pady=10)

ticketno_entry = Entry(line3, bg="#ffffff", width=60, font=("Arial", 14), fg="#0c26af")
ticketno_entry.grid(row=0, column=1, pady=10)

book_button = Button(line3, text="  Cancel Trip  ", bg="#ffffff", fg="#0c26af", padx=5, pady=5, bd=0,
                     activeforeground="#ffffff", activebackground="#0c26af",
                     command=canceltripdetails)
book_button.grid(row=0, column=2, pady=10, padx=15)
book_button.config(font=('Arial', 10, 'bold'))

line3.pack(fill="x", padx=10, pady=5)

# ------------------------------------------------done

line0 = Frame(vframe2, bg="#ffffff")

fontc6 = ("Arial", 22, "bold")

resultl = Label(line0, text="", bg="#ffffff", font=fontc6, fg="#0c26af", padx=10, pady=5)
resultl.grid(row=0, column=0, pady=5, padx=30)

line0.pack(fill="x", padx=10, pady=5, side="top")

line6 = Frame(vframe2, bg="#ffffff")

cancel_button = Button(line6, text=" Back ", bg="#0c26af", fg="white", padx=5, pady=5, bd=0,
                       command=bookflight_window.destroy)
cancel_button.pack(pady=10, padx=5, side="right")
cancel_button.config(font=('Arial', 10, 'bold'))

line6.pack(fill="x", side="bottom", padx=10, pady=10)

vframe2.pack(fill="both", side="top", expand=1, padx=20, pady=20)

mainfame.pack(fill="both", side="top", expand=1)

bookflight_window.mainloop()