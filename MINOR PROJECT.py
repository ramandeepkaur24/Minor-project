from twilio.rest import Client

import phonenumbers
from phonenumbers import geocoder, carrier   ##used for to know company name and country name

from geopy.geocoders import Nominatim

import tkinter
from tkinter import *  ##used for gui window

import tkintermapview
import phonenumbers
import opencage


from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import messagebox
from opencage.geocoder import OpenCageGeocode

from PIL import Image,ImageTk



root=Tk()
root.geometry('360x660')
root.title("EMERGENCY ALARM")
root.resizable(False,False)
root.configure(bg='light blue')

canvas = Canvas(root, height=660, width=360)

canvas.create_rectangle(15,395,345,655,fill="white",outline="black")


canvas.config(bg="light blue")
canvas.pack()

img= ImageTk.PhotoImage(Image.open("images.jpg"))
canvas.create_image(50,430,anchor=NW,image=img)


#HEADING
lb1=Label(root,text='EMERGENCY ALARM',bg="light blue",font="arial 15 bold")
lb1.place(x=80,y=30)


#ICON
image_icon=PhotoImage(file="png-clipart-emergency-service-emergency-telephone-number-oregon-ambulance-miscellaneous-text.png")
root.iconphoto(False,image_icon)

#FUNCTION FOR MESSAGE WITH THE HELP OF TWILIO TEMPORARY KEY
def message():
    SID="ACae7830b909ae8d24c01b194454743b04"
    Auth_Token="1ff3f0e6555ae8e10da793264f1c06e1"

    cl=Client(SID,Auth_Token)

    cl.messages.create(body="PLEASE HELP ME IM IN DANGER",from_="+15735383621",to="+919814662390")

    win = Tk()
    win.title("SENT")
    win.config(bg="white")
    win.geometry("750x95")
    Label(win, text="MESSAGE HAS BEEN SENT",
          font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
    win.after(1200, lambda: win.destroy())
    win.mainloop()

#BUTTON1
image1=PhotoImage(file="msg1.png")
File=Button(root,image=image1,borderwidth=2,command=message)
File.place(x=60,y=100)

#MESSAGE LABEL
lb1=Label(root,text='MESSAGE ',bg="light blue",font="15")
lb1.place(x=55,y=155)

#mapview label
map_label = Label(root, text="MAPVIEW :- ", font=("Calibri", 15, "bold"), bg="light blue")
map_label.place(x=10, y=360)

my_label = LabelFrame(root)
my_label.place(x=30, y=400)


def map():
    locwin = tkinter.Tk()
    locwin.geometry("500x250")
    locwin.title("WHERE I'M")
    locwin.resizable(False,False)

    Label1 = Label(locwin, text="WHERE I'M")
    Label1.pack()

    def getResult():
        num = number.get("1.0", END)
        try:
            num1 = phonenumbers.parse(num)
        except:
            messagebox.showerror("ERROR", "numberbox is empty or input is not numeric!!")

        location = geocoder.description_for_number(num1, "en")
        service_provider = carrier.name_for_number(num1, "en")
        key = 'dab8a5e0cf3c45cebd47f0fb915f269e'  
        ocg = OpenCageGeocode(key)
        query = str(location)
        results = ocg.geocode(query)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        # my_label = LabelFrame(root)
        # my_label.place(x=30,y=400)

        map_widget = tkintermapview.TkinterMapView(my_label, width=300, height=250, corner_radius=0)
        map_widget.set_position(lat, lng)
        map_widget.set_marker(lat, lng, text="PHONE LOCATION")
        map_widget.set_zoom(10)
        map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.S)
        map_widget.pack()


        result.insert(END, "the country of this number is : " + location)
        result.insert(END, "\nthe sim card of this number is : " + service_provider)

        result.insert(END, "\nLatitude is : " + str(lat))
        result.insert(END, "\nLongitude is : " + str(lng))


    number =  Text(locwin,height=1)
    number.pack()

    button = Button(locwin,text="search", command=getResult)
    button.pack(pady=10, padx=100)

    result = Text(locwin,height=7)

    result.pack()


    locwin.mainloop()

#button2
image2=PhotoImage(file="map.png")
File=Button(root,image=image2,borderwidth=2,command=map)
File.place(x=230,y=100)

#where i'm label
lb1=Label(root,text="WHERE I'M",bg="light blue",font="15")
lb1.place(x=225,y=155)



def emg():     #EMERGENCY
    window = Tk()
    window.configure(bg='white')
    window.geometry('590x500')
    window.title("EMEGENCY NUMBER")
    window.resizable(False,False)

    canvas = Canvas(window, height=500, width=600)
    canvas.configure(bg='white')

    srno_lb = Label(window, text="SR_NO", width=7, height=2, borderwidth=3, relief="ridge", font="20", bg="white")
    srno_lb.place(x=2, y=10)

    name_lb = Label(window, text="NAME", width=20, height=2, borderwidth=3, relief="ridge", bg="white", font="20")
    name_lb.place(x=95, y=10)

    connum_lb = Label(window, text="CONTECT", width=10, height=2, borderwidth=3, relief="ridge", bg="white",
                      font="20")
    connum_lb.place(x=490, y=10)

    connum_lb = Label(window, text="CONTECT NUMBER", width=18, height=2, borderwidth=3, relief="ridge", bg="white",
                      font="20")
    connum_lb.place(x=300 , y=10)

    def police():
        account = "ACae7830b909ae8d24c01b194454743b04"
        token = "1ff3f0e6555ae8e10da793264f1c06e1"
        client = Client(account, token)

        call = client.calls.create(to="+919814662390",
                                   from_="+15735383621",
                                   twiml="<Response><Say>I NEED YOUR HELP PLEASE HELP ME</Say></Response>")

        call = Tk()
        call.title("SENT")
        call.config(bg="white")
        call.geometry("550x95")
        Label(call, text="CALL HAS BEEN SENT",
              font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
        call.after(1200, lambda: call.destroy())
        call.mainloop()

    class one():
        lb1 = Label(window, text="1.", font="15", bg="white")
        lb1.place(x=35, y=64)

        lb1 = Label(window, text="POLICE", font="15", bg="white")
        lb1.place(x=98, y=64)

        lb1 = Label(window, text="100", font="15", bg="white")
        lb1.place(x=370, y=64)

        one = Button(window, text="call", borderwidth=2,command=police)
        one.place(x=520, y=63)

    class two():
        lb2 = Label(window, text="2.", font="15", bg="white")
        lb2.place(x=35, y=104)

        lb2 = Label(window, text="108", font="15", bg="white")
        lb2.place(x=370, y=104)

        lb2 = Label(window, text="AMBULANCE", font="15", bg="white")
        lb2.place(x=98, y=104)

        two = Button(window, text="call", borderwidth=2,command=police)
        two.place(x=520, y=103)

    class three():
        lb3 = Label(window, text="3.", font="15", bg="white")
        lb3.place(x=35, y=144)

        lb3 = Label(window, text="1091", font="15", bg="white")
        lb3.place(x=370, y=144)

        lb3 = Label(window, text="WOMEN HELPLINE", font="15", bg="white")
        lb3.place(x=98, y=144)

        three = Button(window, text="call", borderwidth=2,command=police)
        three.place(x=520, y=141)

    class four():
        lb4 = Label(window, text="4.", font="15", bg="white")
        lb4.place(x=35, y=184)

        lb4 = Label(window, text="TRAFFIC HELPLINE", font="15", bg="white")
        lb4.place(x=98, y=184)

        lb4 = Label(window, text="1073", font="15", bg="white")
        lb4.place(x=370, y=181)

        four = Button(window, text="call", borderwidth=2,command=police)
        four.place(x=520, y=181)

    class five():
        lb5 = Label(window, text="5.", font="15", bg="white")
        lb5.place(x=35, y=224)

        lb5 = Label(window, text="FIRE DEPARTMENT", font="15", bg="white")
        lb5.place(x=98, y=224)

        lb5 = Label(window, text="101", font="15", bg="white")
        lb5.place(x=370, y=221)

        five = Button(window, text="call", borderwidth=2,command=police)
        five.place(x=520, y=221)

    class six():
        lb6 = Label(window, text="6.", font="15", bg="white")
        lb6.place(x=35, y=264)

        lb6 = Label(window, text="RAILWAY", font="15", bg="white")
        lb6.place(x=98, y=264)

        lb6 = Label(window, text="139", font="15", bg="white")
        lb6.place(x=370, y=264)

        six = Button(window, text="call", borderwidth=2,command=police)
        six.place(x=520, y=261)

    class seven():
        lb7 = Label(window, text="7.", font="15", bg="white")
        lb7.place(x=35, y=304)

        lb7 = Label(window, text="CYBER CRIME HELPLINE", font="15", bg="white")
        lb7.place(x=98, y=304)

        lb7 = Label(window, text="1930", font="15", bg="white")
        lb7.place(x=370, y=304)

        seven = Button(window, text="call", borderwidth=2,command=police)
        seven.place(x=520, y=301)

    class eight():
        lb8 = Label(window, text="8.", font="15", bg="white")
        lb8.place(x=35, y=344)

        lb8 = Label(window, text="CENTRALISED HELPLINE", font="15", bg="white")
        lb8.place(x=98, y=344)

        lb8 = Label(window, text="112", font="15", bg="white")
        lb8.place(x=370, y=344)

        eight = Button(window, text="call", borderwidth=2,command=police)
        eight.place(x=520, y=341)

    class nine():
        lb9 = Label(window, text="9.", font="15", bg="white")
        lb9.place(x=35, y=384)

        lb9 = Label(window, text="CHILD HELPLINE", font="15", bg="white")
        lb9.place(x=98, y=384)

        lb9 = Label(window, text="1098", font="15", bg="white")
        lb9.place(x=370, y=384)

        nine = Button(window, text="call", borderwidth=2,command=police)
        nine.place(x=520, y=381)

    class ten():
        lb10 = Label(window, text="10.", font="15", bg="white")
        lb10.place(x=35, y=424)

        lb10 = Label(window, text="ANTI CORRPUTION\n HELPLINE", font="15", bg="white")
        lb10.place(x=98, y=424)

        lb10 = Label(window, text="9501200200", font="15", bg="white")
        lb10.place(x=350, y=428)

        ten= Button(window, text="call", borderwidth=2,command=police)
        ten.place(x=520, y=428)

    canvas.create_line(80, 0, 80, 500, fill="black")  # vertical line 1
    canvas.create_line(296, 0, 296, 500, fill="black")  # vertical line 2
    canvas.create_line(0, 57, 600, 57, fill="black")  # horizontal line 1
    canvas.create_line(0, 95, 600, 95, fill="black")  # horizontal line 2
    canvas.create_line(0, 135, 600, 135, fill="black")  # horizontal line 3
    canvas.create_line(0, 175, 600, 175, fill="black")  # horizontal line 4
    canvas.create_line(0, 215, 600, 215, fill="black")  # horizontal line 5
    canvas.create_line(0, 255, 600, 255, fill="black")  # horizontal line 6
    canvas.create_line(0, 295, 600, 295, fill="black")  # horizontal line 7
    canvas.create_line(0, 335, 600, 335, fill="black")  # horizontal line 8
    canvas.create_line(0, 375, 600, 375, fill="black")  # horizontal line 9
    canvas.create_line(0, 415, 600, 415, fill="black")  # horizontal line 10
    canvas.create_line(0, 470, 600, 470, fill="black")  # horizontal line 11
    canvas.create_line(480, 0, 480, 500, fill="black")  # vertical line 12
    canvas.pack()

    window.mainloop()

#EMERGENCY NUMBER button
image3=PhotoImage(file="emglist.png")
File=Button(root,image=image3,borderwidth=2,command=emg)
File.place(x=60,y=220)

#EMERGENCY NUMBER label
lb1=Label(root,text="EMERGENCY\n NUMBER",bg="light blue",font="15")
lb1.place(x=50,y=274)



def police():
    police_root = Tk()
    police_root.geometry('350x350')
    police_root.title("EMERGENCY ALARM")
    police_root.config(bg="#fff")
    police_root.resizable(False, False)

    canvas = Canvas(police_root, height=157, width=300, bg="#fff")
    canvas.create_rectangle(10, 10, 290, 150, fill="white", outline="black")
    canvas.place(x=20,y=150)

    # ps=ImageTk.PhotoImage(file="ps.png")
    lb1 = Label(police_root,text="POLICE STATIONS",font=("Calibri", 17, "bold"),bg="#fff")
    lb1.place(x=98,y=18)


    def show():
        if clicked.get() == "Police Station PS Daba":
            canvas.create_text(150, 50, text="\n          POLICE STATION PS DABA\n\n Address: Main Market, Near Daba Chowk\nLudhiana\nPhone No : 09592914778")
        elif clicked.get() == "Police Station PS Dehlon":
            canvas.create_text(150, 50,text="\n          POLICE STATION PS DEHLON\n\n Address: PRVX+7RC, Malerkotla Rd Dehlon\nDehlon\nPhone No : 9592914070\nEmail : ps.dehlon.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Division No. 5 (Civil Lines)":
                canvas.create_text(150, 50,text="\n          Police Station PS Division No. 5 (Civil Lines)\n\n Address: Near Durga Mata Mandir Ferozepur Road\n Ludhiana-141008\nPhone No : 9592914725\nEmail : ps.div5.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Division No. 6 (Dholewal)":
                canvas.create_text(150, 50,text="\n          Police Station PS Division No. 6 (Dholewal)\n\n Address: Near Dholewal Chowk\n Ludhiana-141003\nPhone No : 9592914726\nEmail : ps.div6.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS DUGRI":
                canvas.create_text(150, 50,text="\n          Police Station PS DUGRI\n\nAddress: Near MD School, MIG Flats\nPhase-1, Dugri , Ludhiana\nPhone No : 9592914776\nEmail : cp.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Focal Point":
                canvas.create_text(150, 50,text="\n          Police Station PS Focal Point\n\n Address: Phase-V, Near Railway Line Focal Point \n Ludhiana-141014\nPhone No : 9592914731\nEmail : ps.fclpnt.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Haibowal":
                canvas.create_text(150, 50,text="\n          Police Station PS Haibowal\n\n Address: Near Pani di tanki, Corporation Park \n Main Bazar, Haibowal, Ludhiana\nPhone No : 9592914733\nEmail : ps.hbwl.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Koom Kalan":
                canvas.create_text(150, 50,text="\n\n         Police Station PS Koom Kalan\n\n Address: Partapgarh to Ratangarh Road \nNear Gurdwara, Koom Kalan\nLudhiana -141126\nPhone No : 9592914738\nEmail : ps.kumkln.khn.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Ladhowal":
                canvas.create_text(150, 50,text="\n          Police Station PS Ladhowal\n\n Address: G.T. Road,Ladhowal Chowk\nLudhiana -141008\nPhone No : 9592914739\nEmail : ps.ldwl.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS N.R.I.":
                canvas.create_text(150, 50,text="\n             Police Station PS N.R.I.\n\n Address: CPRC Building, CP Complex \n Ferozepur Road, Ludhiana\nPhone No : 9592914740\nEmail : complaintcell.nri@punjabpolice.gov.in")
        elif clicked.get() == "Police Station PS Sarabha Nagar":
                canvas.create_text(150, 50,text="\n \n\n         Police Station PS Sarabha Nagar\n\n Address: VRQ3+HRM, Defence Colony\n Bhai Randhir Singh Nagar\n Ludhiana, Punjab 141012\nPhone No : 9592914732\nEmail : ps.srbngr.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Shimlapuri":
                canvas.create_text(150, 50,text="\n   \n\n       Police Station PS Shimlapuri\n\n Address: 12, Gabria Office Rd\n Industrial Area-B, Ludhiana\n Punjab 141003\nPhone No : 9592914730\nEmail : ps.smlpur.ldh.police@punjab.gov.in")
        elif clicked.get() == "Police Station PS Model Town ":
                canvas.create_text(150, 50,text="\n \n   \n      Police Station PS Model Town \n\n Address: Main Market, Pritm Nagar\n Model Town, Ludhiana\n Punjab 141002\nPhone No : 9592914729\nEmail : ps.mdltwn.ldh.police@punjab.gov.in")

    def psmap():
        if clicked.get() == "Police Station PS Daba":
            map_widget = tkintermapview.TkinterMapView(root, width=300, height=250, corner_radius=0)
            map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            map_widget.set_position(30.869663, 75.884112)
            map_widget.set_marker(30.869663, 75.884112, text="POLICE STATION")
            map_widget.set_zoom(10)

            map_widget.set_address("Main Market, Near Daba Chowk,Ludhiana")

        elif clicked.get() == "POLICE STATION PS DEHLON":
            map_widget = tkintermapview.TkinterMapView(root, width=300, height=250, corner_radius=0)
            map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            map_widget.set_position(30.761677, 	75.8766882)
            map_widget.set_marker(30.761677, 	75.8766882, text="POLICE STATION")
            map_widget.set_zoom(10)

            map_widget.set_address("Main Market, Near Daba Chowk,Ludhiana")






    global option
    # Dropdown menu options
    options = [
        "Police Station PS Daba",
        "Police Station PS Dehlon",
        "Police Station PS Division No. 5 (Civil Lines)",
        "Police Station PS Division No. 6 (Dholewal)",
        "Police Station PS DUGRI",
        "Police Station PS Focal Point",
        "Police Station PS Haibowal",
        "Police Station PS Koom Kalan",
        "Police Station PS Ladhowal",
        "Police Station PS N.R.I.",
        "Police Station PS Sarabha Nagar",
        "Police Station PS Shimlapuri",
        "Police Station PS Model Town "
    ]
    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("PS")



    # Create Dropdown menu
    drop = OptionMenu(police_root, clicked, *options)
    drop.place(x=100,y=110)

    # Create button, it will change label text
    button = Button(police_root, text="click Me", command=show,bd=4)
    button.place(x=175,y=108)

    button = Button(police_root, text="MAP",bd=4,command=psmap)
    button.place(x=250,y=108)

    lb1 = Label(police_root, text="LIST:-",font=("Calibri", 12, "bold"), bg="#fff")
    lb1.place(x=40, y=100)


    police_root.mainloop()






#police
image4=PhotoImage(file="police.png")
File=Button(root,image=image4,borderwidth=2,command=police)
File.place(x=230,y=220)

#police station label
lb1=Label(root,text="POLCE\n STATIONS",bg="light blue",font="15")
lb1.place(x=225,y=274)







root.mainloop()