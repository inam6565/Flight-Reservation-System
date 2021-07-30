import sys
from datetime import date
import ni3

def ticket_selector():
    f = open("LIBRARIES\Ticktets_Selector.txt", "rt")

    a = f.read()
    ticketno = int(a) + 1
    f.close()


    f = open("LIBRARIES\Ticktets_Selector.txt", "wt")

    f.write(str(ticketno))

    f.close()
    return ticketno


def reserve_selector():
    f = open("LIBRARIES\Res_Selector.txt", "rt")

    a = f.read()
    rsno = int(a) + 1
    f.close()


    f = open("LIBRARIES\Ticktets_Selector.txt", "wt")

    f.write(str(rsno))

    f.close()






def reserve_data_adderf():
    global  aticketno

    f = open("LIBRARIES\Ticktets_data.txt", "rt")
    if f.read()=="":
        f.close()
        f=open("LIBRARIES\Ticktets_data.txt","wt")
        f.write(str(aticketno))
    else:
        f.close()
        f=open("LIBRARIES\Ticktets_data.txt","at")
        f.write("\n"+str(aticketno) )

        f.close()



def ticktet_data_adder():
    global price, name, lastname, contact, email, gender, age, cnic, aticketno,seatno,flight

    f = open("LIBRARIES\Ticktets_data.txt", "rt")
    if f.read()=="":
        f.close()
        f=open("LIBRARIES\Ticktets_data.txt","wt")
        f.write(str(aticketno) + " " + name + " " + lastname + " " + str(cnic) + " " + email + " " + str(
            contact) + " " + str(
            age) + " " + gender + " " + des + " " + depc + " " + arrc + " " + str(dept) + " " + str(arrt) + " " + str(
            price) + " " + ticketclass + " " + dur + " " + str(ldate) + " " + flight + " " + seatno )
    else:
        f.close()
        f=open("LIBRARIES\Ticktets_data.txt","at")
        f.write("\n"+str(aticketno) + " " + name+" "+lastname+" " + str(cnic)+" "+email+" " + str(contact)+" "+str(age)+" "+gender+ " " + des+" "+depc+ " " + arrc+ " " + str(dept)+" "+str(arrt)+ " " + str(price)+" "+ticketclass+ " " + dur+" "+str(ldate)+" "+flight+" "+seatno)

        f.close()

def bookflight():


    """
    if (ticketstable[date - 1][option - 1][0] + ticketstable[date - 1][option - 1][0] +
        ticketstable[date - 1][option - 1][0]) == 200:
        print("All Class Tickets have been booked !")
        backtomenu()
    """

    global price, name, lastname, contact, email, gender, age, cnic, aticketno, tickets, totaltickets, flight, ticketclass, date, datelist
    global pricelist, namelist, lastnamelist, contactlist, emaillist, cniclist, flightlist, flightsdata, ticketclasslist, agelist
    global seatno, seatnolist,sumclasses,dept,arrt,ticketstatus
    """
    ticketsofthisflight = (ticketstable[date - 1][flight - 1][0] + ticketstable[date - 1][flight - 1][0] +
                           ticketstable[date - 1][flight - 1][0])
    if ticketsofthisflight == 100 or ticketsofthisflight > 100:
        print("Reserve ticket ! ")
        
    """




    aticketno =  ticket_selector()

    # Seat no

    tickets = tickets + 1
    totaltickets = totaltickets + 1


    ni3.ldate=ldate
    ni3.ticketclass=ticketclass
    ni3.flight=flight
    ni3.seatno_gen()
    sumclasses=ni3.sumclasses
    if ticketstatus =="Reserved":
        seatno="Not Assigned"
        reserve_selector()
        reserve_data_adderf()

    else:
        seatno = ni3.seatno

    seatnolist.append(seatno)

    ticketslist.append(aticketno)






    printtickect()


    return


def printtickect():
    global price, name, lastname, contact, email, gender, age, cnic, aticketno, tickets, totaltickets, flight, ticketclass, date, datelist
    global pricelist, namelist, lastnamelist, contactlist, emaillist, cniclist, flightlist, flightsdata, ticketclasslist, agelist
    global seatno, seatnolist,dept,arrt

    filename = "Ticket no." + str(aticketno) + ".txt"
    refund1=(price / 100) * 75
    refund2=(price / 100) * 50
    refund3=(price / 100) * 25
    STR1="2)You will get a refund of " + str(refund1)+ " if you cancel the ticket 48 hours before departure"
    STR2="3)You will get a refund of " + str(refund2)+ " if you cancel the ticket 24 hours before departure"
    STR3="4)You will get a refund of " + str(refund3)+ " if you cancel the ticket 12 hours before departure"



    f = open(filename, "wt")
    f.write("")
    f.close()

    f = open(filename, "at")
    f.write("--------------------------------------------------------------------------------------------------")
    f.write("\n                                   PIA - Airlines  Pakistan                                       ")
    f.write("\n--------------------------------------------------------------------------------------------------")
    f.write("\n Booking No : " + str(aticketno) + "\t\t\t\t\t\tFlight : " + str(flight)           )
    f.write("\n Name : " + name + "\t\t\t\t\tSeat no : " + str(seatno)                                            )
    f.write("\n Last name : " + lastname + "\t\t\t\t\tGender : " + gender                                           )
    f.write("\n Departure : " + str(depc) + "\t\t\t\tArrival : " + str(arrc)       )
    f.write("\n Departure : " + str(dept) + "\t\t\t\tArrival : " + str(arrt)          )
    f.write("\n Contact : " + str(contact) + "\t\t\t\t\t\t\tPrice : " + str(price)                                )
    f.write("\nDate :  " + str(ldate)  + "\t\t\tTicket Class : "  +ticketclass         )
    f.write("\n-------------------------------------------------------------------------------------------------")
    f.write("\n  Note : ")
    f.write("\n       1)You will get a refund of " + str((price)) + " if you cancel the ticket 72 hours before departure")
    f.write("\n       "+STR1)
    f.write("\n       "+STR2)
    f.write("\n       "+STR3)
    f.write("\n       5)You will get no refund if you cancel the ticket less than 12 hours before departure")
    f.write("\n-------------------------------------------------------------------------------------------------")

    f.close()

    ticktet_data_adder()

    return



sumclasses=0

trips = 0
triprefund = 0
ticketstatus="Booked"
ticketclasslist = []
ticketclass = ""
# tickets=[]
today = date.today()
currentdate=today.day

ldate = 0
datelist = []
price = 0
pricelist = []
flight = ""
flightlist = []
flightprices = [[72000, 85000, 90000], [70000, 87000, 95000], [65000, 73000, 80000], [67000, 83000, 90000],
                [66000, 74000, 80000],
                [7500, 8300, 9000], [6900, 7400, 8500], [6500, 7200, 8500], [6800, 7300, 9200], [7400, 8300, 9000]]
name = ""
lastname = ""
email = ""
emaillist = []
namelist = []
lastnamelist = []
contact = 0
contactlist = []
cnic = 0
cniclist = []
gender = ""
genderlist =[]
seatno = ""
seatnolist = []
tickets = 0
ticketslist = []
totaltickets = 0
deletedtickets = 0
deletedticketslist = []
age = 0
agelist = []
aticketno = 0
tripno = 0
tripprice = 0
trippricelist = []
tripfirstindice = []
triplastindice = []

ticketstable=[]

des=""
deslist=[]
depc=""
depclist=[]
dept=""
deptlist=[]

arrc=""
arrclist=[]

arrt=""
arrtlist=[]

dur=""
durlist=[]
