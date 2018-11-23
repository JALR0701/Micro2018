from tkinter import *
from tkinter import ttk
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

Rutina1 = []
Rutina2 = []
Rutina3 = []

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
    x=0
    if(lectura1):
        lectura1 = False
        G1.config(image=BG1)
        G2.config(command=Leer2)
        G3.config(command=Leer3)
        R1.config(command=Enviar1)
        R2.config(command=Enviar2)
        R3.config(command=Enviar3)
    else:
        lectura1 = True
        G1.config(image=Stop)
        G2.config(command=Error)
        G3.config(command=Error)
        R1.config(command=Error)
        R2.config(command=Error)
        R3.config(command=Error)
        del Rutina1 [:]
        
    while(lectura1):
        print("Leyendo1")
        x=x+1
        Rutina1.append(x)
        Main.update()
    return

def Leer2():
    global lectura2
    x=0
    if(lectura2):
        lectura2 = False
        G2.config(image=BG2)
        G1.config(command=Leer1)
        G3.config(command=Leer3)
        R1.config(command=Enviar1)
        R2.config(command=Enviar2)
        R3.config(command=Enviar3)
    else:
        lectura2 = True
        G2.config(image=Stop)
        G1.config(command=Error)
        G3.config(command=Error)
        R1.config(command=Error)
        R2.config(command=Error)
        R3.config(command=Error)
        del Rutina2 [:]
        
    while(lectura2):
        print("Leyendo2")
        x=x+1
        Rutina2.append(x)
        Main.update()
    return

def Leer3():
    global lectura3
    x=0
    if(lectura3):
        lectura3 = False
        G3.config(image=BG3)
        G1.config(command=Leer1)
        G2.config(command=Leer2)
        R1.config(command=Enviar1)
        R2.config(command=Enviar2)
        R3.config(command=Enviar3)
    else:
        lectura3 = True
        G3.config(image=Stop)
        G1.config(command=Error)
        G2.config(command=Error)
        R1.config(command=Error)
        R2.config(command=Error)
        R3.config(command=Error)
        del Rutina3 [:]
        
    while(lectura3):
        print("Leyendo3")
        x=x+1
        Rutina3.append(x)
        Main.update()
    return


##def Timer(Sec):
##    for i in range(sec):
##        sec = sec - 1
##        Time.config(text = ("Faltan " + str(sec) + " Segundos"))
##        time.sleep(1)
##        Main.update()
##    Time.config(text = "")

def Enviar1():
    G1.config(command="")
    G2.config(command="")
    G3.config(command="")
    R1.config(command="", image = Playing)
    R2.config(command="")
    R3.config(command="")
    Barra.config(mode = "indeterminate")
    Barra.start(1)
    Sec = len(Rutina1)*(0.001)
    for V1 in Rutina1:
        print(V1)
        Sec = (Sec - 0.001)
        Time.config(text = ("Faltan " + str(round(Sec*10,1)) + " Segundos"))
        time.sleep(0.001)
        Main.update()
    Barra.config(mode = "determinate")
    Barra.stop()
    Time.config(text = "")
    G1.config(command=Leer1)
    G2.config(command=Leer2)
    G3.config(command=Leer3)
    R1.config(command=Enviar1, image = BR1)
    R2.config(command=Enviar2)
    R3.config(command=Enviar3)
    return

def Enviar2():
    G1.config(command="")
    G2.config(command="")
    G3.config(command="")
    R2.config(command="", image = Playing)
    R1.config(command="")
    R3.config(command="")
    Barra.config(mode = "indeterminate")
    Barra.start(1)
    Sec = len(Rutina2)*(0.001)
    for V2 in Rutina2:
        print(V2)
        Sec = (Sec - 0.001)
        Time.config(text = ("Faltan " + str(round(Sec*10,1)) + " Segundos"))
        time.sleep(0.001)
        Main.update()
    Barra.config(mode = "determinate")
    Barra.stop()
    Time.config(text = "")
    G1.config(command=Leer1)
    G2.config(command=Leer2)
    G3.config(command=Leer3)
    R2.config(command=Enviar2, image = BR2)
    R1.config(command=Enviar1)
    R3.config(command=Enviar3)
    return

def Enviar3():
    G1.config(command="")
    G1.config(command="")
    G3.config(command="")
    R3.config(command="", image = Playing)
    R1.config(command="")
    R2.config(command="")
    Barra.config(mode = "indeterminate")
    Barra.start(1)
    Sec = len(Rutina3)*(0.001)
    for V3 in Rutina3:
        print(V3)
        Sec = (Sec - 0.001)
        Time.config(text = ("Faltan " + str(round(Sec*10,1)) + " Segundos"))
        time.sleep(0.001)
        Main.update()
    Barra.config(mode = "determinate")
    Barra.stop()
    Time.config(text = "")
    G1.config(command=Leer1)
    G2.config(command=Leer2)
    G3.config(command=Leer3)
    R3.config(command=Enviar3, image = BR3)
    R1.config(command=Enviar1)
    R2.config(command=Enviar2)
    return

def Error():
    messagebox.showerror("Error", "Hay una rutina grabando")
    return


Stop = PhotoImage(file = "Stop.PNG")
Playing = PhotoImage(file = "Playing.PNG")

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

Time = Label (Main, text = "", fg = "White", background = "Black")
Time.place(relx=0.5, rely=0.75, width=200, anchor = CENTER)

Barra = ttk.Progressbar(Main, mode="determinate")
Barra.place(relx=0.5, rely=0.8, width=200, anchor = CENTER)


while True:
    Main.update()

