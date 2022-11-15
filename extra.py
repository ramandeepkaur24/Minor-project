import phonenumbers
from phonenumbers import geocoder, carrier,timezone   ##used for to know company name and country name

from geopy.geocoders import Nominatim  ##used for latitude and longitude

import tkinter
from tkinter import *  ##used for gui window

import tkintermapview

locwin=Tk()
locwin.geometry('400x400')
locwin.title("WHERE I'M")
locwin.config(bg="#fff")
locwin.resizable(False,False)


# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("ludhiana")


# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+919814662390")

# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'en')

# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')

# Getting time_zone information
Time_zone = timezone.time_zones_for_number(phoneNumber)

label1=Label(text="COMPANY : " + Carrier, font=("Calibri", 15, "bold"),bg="#fff")
label1.place(x=100,y=60)

label2=Label(text="COUNTRY : " + Region, font=("Calibri", 15, "bold"),bg="#fff")
label2.place(x=100,y=100)

label3=Label(text="TIME_ZONE : " + str(Time_zone), font=("Calibri", 15, "bold"),bg="#fff")
label3.place(x=100,y=220)

label4=Label(text="LATITUDE : " + str(location.latitude), font=("Calibri", 15, "bold"),bg="#fff")
label4.place(x=100,y=140)

label5=Label(text="LONGITUDE : " + str(location.longitude), font=("Calibri", 15, "bold"),bg="#fff")
label5.place(x=100,y=180)

label6=Label(text="DETAIL :- ", font=("Calibri", 20, "bold"),bg="#fff")
label6.place(x=100,y=10)


# def map():
#     root_tk = tkinter.Tk()
#     root_tk.geometry(f"{800}x{600}")
#     root_tk.title("map_view_example.py")
#
#     # create map widget
#     map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
#     map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#     lat = location.latitude
#     lng = location.longitude
#
#     map_widget.set_position(lat, lng)  # Paris, France
#     map_widget.set_zoom(15)
#     map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#     map_widget.pack()
#
#     root_tk.mainloop()
#
#
# File=Button(locwin,text="map",borderwidth=2,command=map)
# File.place(x=150,y=290)



locwin.mainloop()

