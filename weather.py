import requests,json
from tkinter import *
def w(city):
    api = "8a989e2936c9f19c4d83b4c8e19c29fe"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = url + "appid=" + api + "&q=" + city
    x= requests.get(complete_url)
    y=x.json()
    a=[ ]
    a.append(y["main"]["temp"])
    a.append(y["main"]["pressure"])
    a.append(y["main"]["humidity"])
    return(a)
    '''rot = Tk()
    rot.geometry("300x300+100+100")
    can1 = Canvas(width=300,height=300,bg='blue')
    can1.pack()
    p1 = PhotoImage(file="C:\\Users\\Harsh Singh\\Desktop\\AI\\w.png")
    can1.create_image(0,0, image=p1,anchor=NW)
    can1.create_text(20,30,font="Times 20 bold ",fill="Red",text="Temperature :",anchor=NW)
    can1.create_text(200,30,font="Times 20 bold ",fill="Yellow",text=a,anchor=NW)
    can1.create_text(20,80,font="Times 20 bold ",fill="Red",text="Pressure :",anchor=NW)
    can1.create_text(200,80,font="Times 20 bold ",fill="Yellow",text=b,anchor=NW)
    can1.create_text(20,130,font="Times 20 bold ",fill="Red",text="Humidity :",anchor=NW)
    can1.create_text(200,130,font="Times 20 bold ",fill="Yellow",text=c,anchor=NW)
    rot.mainloop()'''


