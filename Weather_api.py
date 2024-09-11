# Python Programming Course : GUI Applications
#                                  -Rahul Mula
# Length Converter ( Meter <-> Inch <-> Foot )

from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0c03b4ef7b55bcfb5b61a830d9ec6008").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    ppr_label1.config(text=data["main"]["pressure"])
    humidity_label1.config(text=data["main"]["humidity"])
    


#city_name="Jaipur"

#data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0c03b4ef7b55bcfb5b61a830d9ec6008").json()

# Main window
app = Tk()
app.title("Weather App")
app.config(bg = "powder blue")
app.geometry("800x800")

name_label=Label(app,text="Weather App",font=("times new roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Rajasthan","Goa","Gujarat",
           
           "Maharashtra","Karnataka","Kerala",
           "Madhya Pradesh","Himachal Pradesh",
           
           "Uttarakhand","Chattisgarh",
           "Arunachal Pradesh","Tamil Nadu"]



com=ttk.Combobox(app,text="Weather App",values=list_name,textvariable=city_name,font=("times new roman",20,"bold"))
com.place(x=25,y=130,height=50,width=450)

#done_button=Button(app,text="Done",font=("times new roman",20,"bold"))
#done_button.place(x=200,y=190,width=100, height=50)




w_label=Label(app,text="Weather Climate",font=("times new roman",20,"bold"))
w_label.place(x=25,y=260,height=50,width=250)

w_label1=Label(app,text="",font=("times new roman",20,"bold"))
w_label1.place(x=300,y=260,height=50,width=250)


wb_label=Label(app,text="Weather description",font=("times new roman",18,"bold"))
wb_label.place(x=25,y=330,height=50,width=250)

wb_label1=Label(app,text="",font=("times new roman",18,"bold"))
wb_label1.place(x=300,y=330,height=50,width=250)

temp_label=Label(app,text="Temperature",font=("times new roman",20,"bold"))
temp_label.place(x=25,y=400,height=50,width=250)

temp_label1=Label(app,text="",font=("times new roman",20,"bold"))
temp_label1.place(x=300,y=400,height=50,width=250)



ppr_label=Label(app,text="Pressure",font=("times new roman",20,"bold"))
ppr_label.place(x=25,y=470,height=50,width=250)

ppr_label1=Label(app,text="",font=("times new roman",20,"bold"))
ppr_label1.place(x=300,y=470,height=50,width=250)


humidity=Label(app,text="Humidity",font=("times new roman",20,"bold"))
humidity.place(x=25,y=550,height=50,width=250)

humidity_label1=Label(app,text="",font=("times new roman",20,"bold"))
humidity_label1.place(x=300,y=550,height=50,width=250)







done_button=Button(app,text="Done",font=("times new roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,width=100, height=50)



app.mainloop()