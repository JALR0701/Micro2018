from tkinter import *
import serial, time

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
lectura = False

def serialR():
    global lectura
    if(lectura):
        lectura = False
        print("False")
    else:
        lectura = True
        print("True")
        
    while(lectura):
        print("Leyendo")
        Main.update()
    return


button = Button(Main, command = serialR).pack()


while True:
    Main.update()

