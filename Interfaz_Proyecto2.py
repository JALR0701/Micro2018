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

Receive1 = "Ángulo del servo 1"
Receive2 = "Ángulo del servo 2"
Receive3 = "Ángulo del servo 3"
Receive4 = "Ángulo del servo 4"

Datos = Label(Main, text = "Autores: Daniel Fuentes y Jorge Lorenzana \nCarné: 17083 y 17302 \n", fg = "White", background = "Black")
Datos.pack()

Servo1 = Label(Main, text = "Servo 1", fg = "White", background = "Black")
Servo1.place (relx=0.2, rely=0.25, anchor=CENTER)

Angulo1 = Label(Main, text = Receive1, borderwidth=1, relief="solid", fg = "White", background = "Black")
Angulo1.place (relx=0.2, rely=0.3, anchor=CENTER)

Servo2 = Label(Main, text = "Servo 2", fg = "White", background = "Black")
Servo2.place (relx=0.4, rely=0.25, anchor=CENTER)

Angulo2 = Label(Main, text = Receive2, borderwidth=1, relief="solid", fg = "White", background = "Black")
Angulo2.place (relx=0.4, rely=0.3, anchor=CENTER)

Servo3 = Label(Main, text = "Servo 3", fg = "White", background = "Black")
Servo3.place (relx=0.6, rely=0.25, anchor=CENTER)

Angulo3 = Label(Main, text = Receive3, borderwidth=1, relief="solid", fg = "White", background = "Black")
Angulo3.place (relx=0.6, rely=0.3, anchor=CENTER)

Servo4 = Label(Main, text = "Servo 4", fg = "White", background = "Black")
Servo4.place (relx=0.8, rely=0.25, anchor=CENTER)

Angulo4 = Label(Main, text = Receive4, borderwidth=1, relief="solid", fg = "White", background = "Black")
Angulo4.place (relx=0.8, rely=0.3, anchor=CENTER)

Main.mainloop()
