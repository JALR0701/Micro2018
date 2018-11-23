from tkinter import *
import serial, time
from tkinter import messagebox

##while(1):
##    while(1):
##        try:
##            Puerto = "com" + str(int(input(">  COM: ")))
##            break
##        except:
##            print ("Ingrese el numero de COM") 
##    try:
##        Pic = serial.Serial(Puerto, baudrate = 9600, timeout=1500, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
##        break
##    except:
##        print("Puerto Incorrecto")

Main = Tk()
Main.title("Comunicación serial")
w = 700 
h = 700

ws = Main.winfo_screenwidth()
hs = Main.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

Main.geometry('%dx%d+%d+%d' % (w, h, x, y))
Main.resizable(0,0)
Main. config (background = "Black")

Datos = Label(Main, text = "Autores: Daniel Fuentes y Jorge Lorenzana \nCarnés: 17083 y 17302 \n", fg = "White", background = "Black")
Datos.pack()

Rutina = []

##Vin = None
##Pic.reset_input_buffer()
##time.sleep(.1)
##while(Vin is None):
##    Vin = Pic.readline(1)
##Vin = ord(Vin)
lectura1 = False
lectura2 = False
lectura3 = False


def Leer1():
    global lectura1
    if(lectura1):
        lectura1 = False
        G1.config(image=BG1)
        G2.config(command=Leer2)
        G3.config(command=Leer3)
    else:
        lectura1 = True
        G1.config(image=Stop)
        G2.config(command=Error)
        G3.config(command=Error)
        
    while(lectura1):
        print("Leyendo1")
        Main.update()
    return

def Leer2():
    global lectura2
    if(lectura2):
        lectura2 = False
        G2.config(image=BG2)
        G1.config(command=Leer1)
        G3.config(command=Leer3)
    else:
        lectura2 = True
        G2.config(image=Stop)
        G1.config(command=Error)
        G3.config(command=Error)
        
    while(lectura2):
        print("Leyendo2")
        Main.update()
    return

def Leer3():
    global lectura3
    if(lectura3):
        lectura3 = False
        G3.config(image=BG3)
        G1.config(command=Leer1)
        G2.config(command=Leer2)
    else:
        lectura3 = True
        G3.config(image=Stop)
        G1.config(command=Error)
        G2.config(command=Error)
        
    while(lectura3):
        print("Leyendo3")
        Main.update()
    return

def Enviar1():
    return

def Enviar2():
    return

def Enviar3():
    return

def Error():
    messagebox.showerror("Error", "Hay una rutina grabando")
    return

Stop = PhotoImage(file = "Stop.PNG")

BG1 = PhotoImage(file="Boton_G1.PNG")
BG2 = PhotoImage(file="Boton_G2.PNG")
BG3 = PhotoImage(file="Boton_G3.PNG")

G1 = Button(Main, command = Leer1, image=BG1, bg = "Black", border = 0)
G1.place(relx=0.2, rely=0.3)
G2 = Button(Main, command = Leer2, image=BG2, bg = "Black", border = 0)
G2.place(relx=0.1, rely=0.45)
G3 = Button(Main, command = Leer3, image=BG3, bg = "Black", border = 0)
G3.place(relx=0.3, rely=0.45)

BR1 = PhotoImage(file="Boton_R1.PNG")
BR2 = PhotoImage(file="Boton_R2.PNG")
BR3 = PhotoImage(file="Boton_R3.PNG")

R1 = Button(Main, command = Enviar1, image=BR1, bg = "Black", border = 0)
R1.place(relx=0.7, rely=0.3)
R2 = Button(Main, command = Enviar2, image=BR2, bg = "Black", border = 0)
R2.place(relx=0.6, rely=0.45)
R3 = Button(Main, command = Enviar3, image=BR3, bg = "Black", border = 0)
R3.place(relx=0.8, rely=0.45)


while True:
    Main.update()

