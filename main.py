import requests
from tkinter import *
root=Tk()
root.geometry("500x500")

city_label=Label(root,text="city")
city_label.place(x=100,y=100)

region_label=Label(root,text="Region")
region_label.place(x=100,y=150)

country_label=Label(root,text="Country")
country_label.place(x=100,y=200)

Postal_label=Label(root,text="Postal")
Postal_label.place(x=100,y=250)

Time=Label(root,text="Time")
Time.place(x=100,y=300)

org=Label(root,text="Org")
org.place(x=100,y=350)


#textboxes
city_text=Text(root,height=1,width=20)
city_text.place(x=150,y=100)


#function part

def live_loc():

    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']
    # city.config(city_text.get(1.0,"end-1c"))

    region = data['region']
    country = data['country']
    postal = data['postal']
    timezone = data['timezone']
    org = data['org']


    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]



    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("City : ", city)
    print("region : ",region)
    print("country : ",country)
    print("postal : ",postal)
    print("timezone : ",timezone)
    print("org : ",org)


File=Button(root,text="show details",borderwidth=2,command=live_loc)
File.place(x=230,y=320)




root.mainloop()