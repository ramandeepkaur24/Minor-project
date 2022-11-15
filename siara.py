import tkinter
import tkintermapview
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage

from tkinter import *
from tkinter import messagebox
from opencage.geocoder import OpenCageGeocode


root=tkinter.Tk()
root.geometry("500x850")
root.title("WHERE I'M")

Label1=Label(root,text="WHERE I'M")
Label1.pack()

def getResult():
    num = number.get("1.0",END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("ERROR","numberbox is empty or input is not numeric!!")

    location = geocoder.description_for_number(num1,"en")
    service_provider = carrier.name_for_number(num1,"en")
    key='dab8a5e0cf3c45cebd47f0fb915f269e'
    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label,width=450,height=450,corner_radius=0)
    map_widget.set_position(lat,lng)
    map_widget.set_marker(lat,lng,text = "PHONE LOCATION")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    map_widget.pack()

        #adr = tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END,"the country of this number is : " + location)
    result.insert(END,"\nthe sim card of this number is : " + service_provider)

    result.insert(END, "\nLatitude is : " + str(lat))
    result.insert(END, "\nLongitude is : " + str(lng))

         #result.insert(END,"\nStreet address is : " + adr.street)
        # result.insert(END,"\ncity address is : " + adr.city)
         #result.insert(END,"\nPostal code is : " + adr.postal)

number=Text(height=1)
number.pack()

button = Button(text="search",command=getResult)
button.pack(pady = 10,padx=100)

result=Text(height=7)
result.pack()


root.mainloop()