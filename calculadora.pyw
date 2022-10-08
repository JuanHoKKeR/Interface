from sys import float_repr_style
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Style


raiz=Tk()

miFrame=Frame(raiz)
raiz.title("CALCULADORA")
raiz.iconbitmap("calcu.ico")
raiz.resizable(1,1)
miFrame.pack()
miFrame.config(relief="groove",cursor="hand2",bd=10,bg="#4D4642")

operacion=""
resultado=0
auxiliar=""
#-----------------PANTALLA----------------------------------
numero_pantalla=StringVar()


pantalla=Entry(miFrame,textvariable=numero_pantalla)
pantalla.grid(row="1",column="1",padx="2",pady="2",columnspan=5)
pantalla.config(background="#86CB71",fg="black",justify="right",bd=5,font=("Courier", 12,"bold"))

#----------------PULSACIONES TECLADO----------------------
def numeroPulsado(num):
    global operacion
    punto=0
    if operacion != "":
            numero_pantalla.set(num)
            operacion=""
    else:
        if num==".":
            for i in numero_pantalla.get():
                if i==".":
                    punto+=1
            if punto<1:
                numero_pantalla.set(numero_pantalla.get()+num)
        elif num=="0":
            if numero_pantalla.get()=="":
                pass
            else:
                numero_pantalla.set(numero_pantalla.get()+num)
        else:
            numero_pantalla.set(numero_pantalla.get()+num)

#---------------FUNCION SUMA-----------------------
def suma(num):
    global operacion
    global resultado
    global auxiliar
    resultado+=float(num)
    operacion="suma"
    auxiliar=operacion
    numero_pantalla.set(resultado)

#---------------FUNCION RESTA-----------------------
def resta(num):
    global operacion
    global resultado
    global auxiliar
    if resultado==0:
        resultado=float(num)
    else:
        resultado=float(num)-resultado
    operacion="resta"
    auxiliar=operacion
    numero_pantalla.set(resultado)


#---------------FUNCION MULTIPLICACION-----------------------
def multiplicar(num):
    global operacion
    global resultado
    global auxiliar
    if resultado==0:
        resultado=float(num)
    else:
        resultado*=float(num)
    operacion="multiplicacion"
    auxiliar=operacion
    numero_pantalla.set(resultado)


#---------------FUNCION DIVISION-----------------------
def dividir(num):
    global operacion
    global resultado
    global auxiliar
    if num=="0" or num==".":
        numero_pantalla.set("No es posible divider sobre 0")
    else:
        resultado=float(num)
        operacion="divide"
        numero_pantalla.set(resultado)
        auxiliar=operacion


#--------------RESULTADO---------------------
def resul():
    global resultado
    global operacion
    global auxiliar
    if auxiliar=="suma":
        numero_pantalla.set(resultado+float(numero_pantalla.get()))
    elif auxiliar=="resta":
        numero_pantalla.set(resultado-float(numero_pantalla.get()))
    elif auxiliar=="multiplicacion":
        numero_pantalla.set(resultado*float(numero_pantalla.get()))
    elif auxiliar=="divide":
        try:
            numero_pantalla.set(resultado/float(numero_pantalla.get()))
        except ZeroDivisionError:
            numero_pantalla.set("ERROR")
    resultado=0
    auxiliar=""

#--------------BORRAR------------------------
def borrar():
    global resultado
    resultado=0
    numero_pantalla.set("")


#--------------CAMBIA------------------------
def cambia():
    if numero_pantalla.get()=="":
        numero_pantalla.set("-")
    else:
        numero_pantalla.set((-1)*float(numero_pantalla.get()))

#---------------------BOTONES------------------------------
#************FILA 1*******************
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row="2",column="1")
boton7.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row="2",column="2")
boton8.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row="2",column="3")
boton9.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_borrar=Button(miFrame,text="DEL",width=3,command=lambda:borrar())
boton_borrar.grid(row="2",column="4",columnspan=2)
boton_borrar.config(background="#FC6700",font=("Courier", 10, "italic","bold"),bd=5,width=8)

#**************FILA2******************
boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row="3",column="1")
boton4.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row="3",column="2")
boton5.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row="3",column="3")
boton6.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_multi=Button(miFrame,text="X",width=3,command=lambda:multiplicar(numero_pantalla.get())) #MULTIPLICAR
boton_multi.grid(row="3",column="4")
boton_multi.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_div=Button(miFrame,text="/",width=3,command=lambda:dividir(numero_pantalla.get()))  #DIVIDIR
boton_div.grid(row="3",column="5")
boton_div.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)


#*************FILA3*******************
boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row="4",column="1")
boton1.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row="4",column="2")
boton2.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row="4",column="3")
boton3.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_suma=Button(miFrame,text="+",width=3,command=lambda:suma(numero_pantalla.get())) #SUMA
boton_suma.grid(row="4",column="4")
boton_suma.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_res=Button(miFrame,text="-",width=3,command=lambda:resta(numero_pantalla.get())) #RESTA
boton_res.grid(row="4",column="5")
boton_res.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

#************FILA4********************
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row="5",column="1")
boton0.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_punto=Button(miFrame,text=".",width=3,command=lambda:numeroPulsado("."))
boton_punto.grid(row="5",column="2")
boton_punto.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_x=Button(miFrame,text="+/-",width=3,command=lambda:cambia())
boton_x.grid(row="5",column="3")
boton_x.config(background="black",fg="white",font=("Courier", 10, "italic","bold"),bd=5)

boton_igual=Button(miFrame,text="=",width=3,command=lambda:resul()) #RESULTADO
boton_igual.grid(row="5",column="4",columnspan=2)
boton_igual.config(background="gray",fg="black",font=("Courier", 10, "italic","bold"),bd=5,width=8)










raiz.mainloop()