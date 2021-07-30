from tkinter import *
from subprocess import call

def list_of_flight():
    call(["python","LIST_OF_FLIGHTS_GUI.py"])
def flight_information():
    call(["python", "FLIGHT_INFO_GUI.py"])
def book_flight():
    call(["python","BOOKING_GUI.py"])
def cancel_flight():
    call(["python", "CANCEL_FLIGHT_GUI.py"])
def view_booking():
    call(["python", "VIEW_BOOKING_DETAILS_GUI.py"])
def search_flight():
    call(["python","SEARCH_GUI.py"])
def search_ticket():
    call(["python", "SEARCH_TICKET_GUI.py"])
def create_trip():
    call(["python", "CREATE_TRIP_GUI.py"])
def cancel_trip():
    call(["python", "CANCEL_TRIP_GUI.py"])






window=Tk()
window.title("Flight Reservation system            Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar DSA CEP BEE 56 D")
window.geometry('1500x730')
mainframe=Frame(window,bg="white")
window.iconbitmap('images/icon1.ico')
mainframe.pack(fill="both",expand=TRUE)
#Images
p11=PhotoImage(file ="images/p11.gif")

f111=PhotoImage(file ="images/home_icon_white.gif")


f1=PhotoImage(file ="images/f1.gif")
f2=PhotoImage(file ="images/f2.gif")
f3=PhotoImage(file ="images/f3.gif")
f4=PhotoImage(file ="images/f4.gif")
f5=PhotoImage(file ="images/f5.gif")
f6=PhotoImage(file ="images/f6.gif")
f7=PhotoImage(file ="images/f7.gif")
f8=PhotoImage(file ="images/f8.gif")
f9=PhotoImage(file ="images/f9.gif")
p101=PhotoImage(file ="images/p101.gif")


#00B050


#Bottom Status bar
status=Label(text="Copyrights © 2021.Hadia Saif | Hadia Ushaq | Inam ur Rehman | Muhammad Tayyab Gulzar . All Copyrights reserved.",bg="black",fg="white",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",10))
status.pack(fill="x",side="bottom")

"""
#Footer logo
logoframe=Frame(mainframe,bg="#ffffff",relief=FLAT,bd=0)
logoframe.pack(side="bottom",fill="x")

logo1=Label(logoframe,image=img,relief=FLAT,bd=0)
logo1.pack(side="left")
"""

#Header logo
logoframe=Frame(mainframe,bg="#ffffff",relief=FLAT,bd=0)
logoframe.pack(side="top",fill="x")

logo1=Label(logoframe,image=p11,relief=FLAT,bd=0)
logo1.pack(side="left")

#Top Status bar
status=Label(mainframe,text="   Home",image=f111,compound=LEFT,bg="#00B050",fg="white",bd=10,relief=FLAT,anchor=W)
status.config(font=("Arial",12))
status.pack(fill="x",side="top")



#Left side logo

logoframe1=Frame(mainframe,bg="#ffffff",relief=FLAT,bd=0)
logoframe1.pack(side="left",fill="y")

logo1=Label(logoframe1,image=p101,relief=FLAT,bd=0)
logo1.pack(side="left")


#Right side logo

logoframe1=Frame(mainframe,bg="#ffffff",relief=FLAT,bd=0)
logoframe1.pack(side="right",fill="y")

logo1=Label(logoframe1,image=p101,relief=FLAT,bd=0)
logo1.pack(side="right")




#Menu Frame


menu=Frame(mainframe,bg="white",padx=5,pady=5)

#Buttons
"""
label10=Label(root,text="Tkinter SOLID",bg="black",fg="white",width=30,height="5",bd=5,relief=SOLID,cursor="shuttle")
label10.pack(side="bottom",padx=5,pady=5)
"""
#Button 1
button_list_of_flight = Button(menu,image=f1,bg="gray",bd=0,fg="white",command=list_of_flight)
button_list_of_flight.grid(row=0, column=0)
menu.grid_columnconfigure(0, weight=1)

#Button 2
flight_info = Button(menu,image=f2,bg="gray",bd=0,fg="white",command=flight_information)
flight_info.grid(row=0, column=1)
menu.grid_columnconfigure(0, weight=1)

#Button 3
book_flight_button = Button(menu,image=f3,bg="gray",bd=0, fg="white",command=book_flight)
book_flight_button.grid(row=0, column=2)
menu.grid_columnconfigure(0, weight=1)

#Button 4
cancel_flight = Button(menu,image=f4, bg="gray",bd=0, fg="white", padx=5, pady=5,command=cancel_flight)
cancel_flight.grid(row=1, column=0)
menu.grid_columnconfigure(0, weight=1)

#Button 5
view_book_detail = Button(menu,image=f5, bg="gray",bd=0, fg="white", padx=5, pady=5,command=view_booking)
view_book_detail.grid(row=1, column=1)
menu.grid_columnconfigure(1, weight=1)

#Button 6
search_flight = Button(menu,image=f6, bg="gray", bd=0,fg="white", padx=5, pady=5,command=search_flight)
search_flight.grid(row=1, column=2)
menu.grid_columnconfigure(2, weight=1)

#Button 7
search_ticket = Button(menu, image=f7 ,bg="gray", bd=0,fg="white", padx=5, pady=5,command=search_ticket)
search_ticket.grid(row=2, column=0)
menu.grid_columnconfigure(0, weight=1)

#Button 8
create_trip = Button(menu,image=f8,bg="gray", bd=0,fg="white", padx=5, pady=5,command=create_trip)
create_trip.grid(row=2, column=1)
menu.grid_columnconfigure(1, weight=1)

#Button 9
cancel_trip = Button(menu,image=f9, bg="gray",bd=0, fg="white", padx=5, pady=5,command=cancel_trip)
cancel_trip.grid(row=2, column=2)
menu.grid_columnconfigure(2, weight=1)

menu.pack(fill="x",side="bottom",padx=5,pady=5)


window.mainloop()


