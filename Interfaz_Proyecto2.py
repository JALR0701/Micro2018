from tkinter import *
import serial, time

while(1):
    while(1):
        try:
            Puerto = "com" + str(int(input(">  COM: ")))
            break
        except:
            print ("Ingrese el numero de COM") 
    try:
        Pic = serial.Serial(Puerto, baudrate = 9600, timeout=1500, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
        break
    except:
        print("Puerto Incorrecto")


def SendValue ():
    Sending = angulo.get()
    
    while (1):
        try:
            Sending = float(Sending)
            break
        except:
            Text.set("Ingrese un valor dentro de los límites")
            Error.config (fg = "red")
            return
        
    if (not(float(Sending)>= 0 and float(Sending)<= 180)):
        Text.set("Ingrese un valor dentro de los límites")
        Error.config (fg = "red")
    else:
        Sending = int(Sending)
        Sending = int(((Sending/180)*28)+10)
        Sending = bytes([Sending])
        Pic.write(Sending)
        print(Sending)
        Text.set("Enviado")
        Error.config (fg = "green")
    return

def update():
    Vin = None
    Pic.reset_input_buffer()
    time.sleep(.1)
    while(Vin is None):
        Vin = Pic.readline(1)
    Vin = ord(Vin)
    Vin = round((Vin * 5)/255, 2)
    Receive = str(Vin) + " V"
    Valor.config(text=Receive)
    Main.after(500, update)
    return
        

Main = Tk()
Main.title("Comunicación serial")
w = 500 
h = 500

Text = StringVar()
angulo = IntVar()

Vin = None
Pic.reset_input_buffer()
time.sleep(.1)
while(Vin is None):
    Vin = Pic.readline(1)
Vin = ord(Vin)
Vin = round((Vin * 5)/255, 2)
Receive = str(Vin) + " V"

ws = Main.winfo_screenwidth()
hs = Main.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

Main.geometry('%dx%d+%d+%d' % (w, h, x, y))
Main.resizable(0,0)
Main. config (background = "Black")

Datos = Label(Main, text = "Autor: Jorge Lorenzana \nCarné: 17302 \n", fg = "White", background = "Black")
Datos.pack()

Voltaje = Label(Main, text = "Voltaje entrando", fg = "White", background = "Black")
Voltaje.place (relx=0.5, rely=0.25, anchor=CENTER)

Valor = Label(Main, text = Receive, borderwidth=1, relief="solid", fg = "White", background = "Black")
Valor.place (relx=0.5, rely=0.3, anchor=CENTER)

Ángulo = Label(Main, text = "Ingrese el ángulo del servo", fg = "White", background = "Black")
Ángulo.place (relx=0.5, rely=0.5, anchor=CENTER)

Posicion = Entry(Main, textvariable = angulo)
Posicion.place (relx=0.5, rely=0.55, anchor=CENTER)

Send = Button (Main, text = "Enviar", command = SendValue)
Send.place (relx=0.5, rely=0.6, anchor=CENTER)

Error = Label(Main, textvariable = Text, background = "Black")
Error.place(relx=0.5, rely=0.65, anchor=CENTER)

Main.after(500, update)
Main.mainloop()
