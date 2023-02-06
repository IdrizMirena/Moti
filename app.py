'''
App per Motin
'''

#imports
import tkinter as tk
import requests
import time
from PIL import ImageTk,Image

#motiyn func me canvas
def moti_yn(canvas):
    qyteti = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+qyteti+"&appid=06c921750b9a82d8f5d1294e1586276f"  #Kjo eshte api e webit ku e shikon motin
    '''
     Modifikimi i temperaturave dhe zhvillimi i llojeve te tyre
    '''
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main'] 

    temperatura = int(json_data['main']['temp'] - 273.15)

    temperatura_minimale = int(json_data['main']['temp_min'] - 273.15)

    temperatura_maksimale = int(json_data['main']['temp_max'] - 273.15)

    Presioni = json_data['main']['pressure']

    Lageshtia = json_data['main']['humidity']

    era = json_data['wind']['speed']

    Lindja_e_diellit = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))

    Perendimi_i_diellit = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    infotfinale = condition + "\n" + str(temperatura) + "°C" 
    tedhenatfinale = "\n"+ "Temperatura Minimale : " + str(temperatura_minimale) + "°C" + "\n" + "Temperatura Maksimale : " + str(temperatura_maksimale) + "°C" +"\n" + "Presioni : " + str(Presioni) + "\n" +"Lagështi : " + str(Lageshtia) + "\n" +"Shpejtsia e eres : " + str(era) + "\n" + "Lindja e diellit : " + Lindja_e_diellit + "\n" + "Perendimi i diellit : " + Perendimi_i_diellit
    label1.config(text = infotfinale)
    label2.config(text = tedhenatfinale)


canvas = tk.Tk()
canvas.geometry("700x500")
canvas.title("App Moti | Idriz Mirena")
x = ("poppins", 15, "bold")
y = ("poppins", 35, "bold")

#img =tk.PohtoImage(file='pohto.png')
#canvas.create_image(20,20, anchor=NW,image=img)      ''' BG

#background_image=tk.PhotoImage('pohto.png')
#ackground_label=tk.Label(canvas,image=background_image)   ''' BG2
#background_label.place(x=0,y=0,relwidth=1,relheight=2)

textField = tk.Entry(canvas, justify='center', width = 30, font = y)  # permasat ne grafik
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', moti_yn)
label1 = tk.Label(canvas, font=y)
label1.pack()
label2 = tk.Label(canvas, font=x)
label2.pack()
canvas.mainloop()
