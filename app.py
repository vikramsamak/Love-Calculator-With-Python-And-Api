from tkinter import*
from pprint import pp
from tkinter.ttk import Labelframe
import requests
import json

def calculate():
    sname=ent1.get()
    fname=ent2.get()
    
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    
    querystring = {"sname":sname,"fname":fname}
    
    headers = {
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": "36c760c943msh54bb49a0d0bc726p1fedccjsn1fc39ca84a67"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res=response.json()

    percentage=res['percentage']

    result=res['result']

    lbl3.config(text="Percentage Of Love:"+percentage +"%")
    lbl4.config(text="Result:"+result)



window=Tk()
window.title("Love Calculator")
window.geometry('350x400')
window.minsize(350,400)
window.maxsize(350,400)

mainframe=Labelframe(window,width=100)
mainframe.pack()

lbl1=Label(mainframe,text="Enter Your Name:",font=("Arial",15))
lbl1.pack(pady=15)

ent1=Entry(mainframe,font=("Arial",15))
ent1.pack(pady=15)

lbl2=Label(mainframe,text="Enter Your Crush's Name:",font=("Arial",15))
lbl2.pack(pady=15)

ent2=Entry(mainframe,font=("Arial",15))
ent2.pack(pady=15)

btn1=Button(mainframe,text="Calculate Percentage of Love",font=("Arial",15),command=calculate)
btn1.pack(pady=15)

lbl3=Label(mainframe,text="",font=("Arial",15))
lbl3.pack()

lbl4=Label(mainframe,text="",font=("Arial",15))
lbl4.pack()

window.mainloop()