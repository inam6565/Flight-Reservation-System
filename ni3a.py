


global sumclasses,ldate,flight,ticketclass,seatno,eseats,aseats,bseats

def seat_update(e,a,b,ct):
    global ticketclass, ldate, flight, seatno,sumclasses,eseats,aseats,bseats
    eseats = int(e)
    aseats = int(a)
    bseats = int(b)
    with open('LIBRARIES\Seat_Generator2.txt', 'r') as datafile:
        entireDataText = datafile.read()


    with open('LIBRARIES\Seat_Generator2.txt', 'w') as datafile:
        lines = entireDataText.split('\n')
        edittedLine = lines[int(ct) - 1].split()


        prefix = ""
        if ticketclass == "Select":
            sumclasses = int(e) + int(a) + int(b)
            seatno = "Not Assigned"



            print()
        elif ticketclass == "Economy":
            prefix = "E"
            x = int(e) + 1

            sumclasses=int(x)+int(a)+int(b)
            edittedLine[2] = str(x)

            edittedLine[-1] = str(sumclasses)

            seatno = flight + "-" + prefix + "-" + str(x)
        elif ticketclass == "A-Class":
            prefix = "A"
            print(a)
            y = int(a) + 1

            edittedLine[3] = str(y)
            sumclasses=int(e)+int(y)+int(b)
            edittedLine[-1] = str(sumclasses)

            seatno = flight + "-" + prefix + "-" + str(y)
        elif ticketclass == "Business":
            prefix = "B"
            z = int(b) + 1

            edittedLine[4] = str(z)
            sumclasses=int(e)+int(a)+int(z)
            edittedLine[-1] = str(sumclasses)

            seatno = flight + "-" + prefix + "-" + str(z)

        lines[int(ct) - 1] = ' '.join(edittedLine)
        entireDataText = '\n'.join(lines)
        datafile.write(entireDataText)
    return


def first_append():
    global ticketclass,ldate,flight,seatno,sumclasses,eseats,aseats,bseats
    f = open("LIBRARIES\Seat_Generator2.txt", "at")
    seatno=""
    e = 0
    a = 0
    b = 0
    prefix=""

    if ticketclass == "Select":
        sumclasses = int(e) + int(a) + int(b)
        seatno ="Not Assigned"
        eseats = int(e)
        aseats = int(a)
        bseats = int(b)



    if ticketclass == "Economy":
        prefix="E"
        e=e+1
        seatno = flight + "-" + prefix + "-" +str(e)
    elif ticketclass == "A-Class":
        prefix = "A"
        a=a+1
        seatno = flight + "-" + prefix + "-" +str(a)
    elif ticketclass == "Business":
        prefix = "B"
        b=b+1
        seatno = flight + "-" + prefix + "-" +str(b)

    f.write(ldate+" "+flight+" "+str(e)+" "+str(a)+" "+str(b)+" "+str(e+a+b)+"\n")
    f.close()


def seatno_gen():
    with open("LIBRARIES\Seat_Generator2.txt","rt") as f:
        n = f.read()
        ab=False
        if n == "":
            first_append()

        else:
            entireDataText = f.read()
            f.seek(0, 0)
            ct=0
            for line in f:
                ct += 1
                if ldate == line.split()[0] and flight == line.split()[1]:
                    e=line.split()[2]
                    a=line.split()[3]
                    b=line.split()[4]
                    ab=False
                    seat_update(e,a,b,ct)
                    break
                else:
                    ab=True

        if ab==True:
            first_append()




