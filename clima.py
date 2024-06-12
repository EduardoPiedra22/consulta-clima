import  tkinter as tk
import requests
windows = tk.Tk()
windows.title ("Clima Mundial")
# Configuracion de  Dimensiones:
windows.geometry("600x300")

etiqueta = tk.Label(windows, text="Ingrese la ciudad  o pais que deseea consulta su temperatura: ")
etiqueta.pack()
localitation = tk.Entry(windows, width=30)
localitation.pack()

def consul_Clima ():
    city = localitation.get()
    api_key = ("167e66dedd490de6a53f2b49f1bc169e")
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    consulta = requests.get(url)
    if consulta.status_code == 200:
        json = consulta.json()
        temp = json["main"]["temp"]
        descripcion = json['weather'][0]['description']
        resultado.config(text=f"La Temperatura de {city} es : {temp}°C\nDescripción: {descripcion}")
    else:
        resultado.config(text="Pais o ciudad no valido")
        

boton = tk.Button(windows, text='Consultar', command=consul_Clima)
boton.pack()
resultado = tk.Label(windows, text="")
resultado.pack()
windows.mainloop()

