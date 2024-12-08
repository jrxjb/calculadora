from tkinter import * 
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
icon_path = os.path.join(current_dir, 'cat.ico')


global cadena
cadena=""
global cadena2 
cadena2=""
global variableC
variableC=""
global Reloj
Reloj=""
S=0
global cuenta2
cuenta2=0
M=0     #minutos 
H=0     #horas
D=0     #dias
M2=0   # minutos restantes es pués se una pausa
H2=0
D2=0
def sumar():
    global cadena
    global cadena2 
    global variableC
    try:
        cadena=float(variableA.get())
        variableA.set(float(cadena2)+float(cadena))
        valorDeA.config(bg="silver") 
        cadena=""
        cadena2=""
    except:
            variableA.set("Error")
            valorDeA.config(bg="red") 
            cadena=""
            cadena2=""
def restar():
   global cadena
   global cadena2
   try:
    cadena=float(variableA.get())
    variableA.set(float(cadena2)-float(cadena))
    valorDeA.config(bg="silver") 
    cadena=""
    cadena2=""
   except:
            variableA.set("no es un numero")
            valorDeA.config(bg="red") 
            cadena=""
            cadena2=""


def multiplicar():
   global cadena
   global cadena2
   try:
    cadena=float(variableA.get())
    variableA.set(float(cadena2)*float(cadena))
    valorDeA.config(bg="silver") 
    cadena=""
    cadena2=""
   except:
            variableA.set("no es un numero")
            valorDeA.config(bg="red")     
            cadena=""
            cadena2=""
    
def dividir():
   global cadena
   global cadena2
   try:
    cadena=float(variableA.get())
    variableA.set(float(cadena2)/float(cadena))
    valorDeA.config(bg="silver") 
    cadena=""
    cadena2=""
   except:
            variableA.set("no es un numero")
            valorDeA.config(bg="red") 
            cadena=""
            cadena2=""

def calculoTiempoRestante():
    global cuenta2
    global S
    divisor = 60
    global M2
    M2, residuo = divmod(cuenta2, divisor)
    cuenta2=cuenta2+residuo
    print(f"S:{cuenta2}, M2:{M2}")
    actualizar()

def actualizar():
     global Reloj
     global S
     global cuenta2
     global M
     global D
     global H
     global M2
     global H2
     global D2
     divisor = 60
     divisorDias= 24
     #Ron

     if (Reloj==1):
          S=S+1+cuenta2
          cuenta2=0
          M=M+M2
          M2=0
          H=H+H2
          H2=0
          D=D+D2
          D2=0
          if(S>60):
               M2, residuo = divmod(S, divisor)
               S=residuo
               print(f"S:{S}, M2:{M2}")
              # palabra.set(f"{D}:{H}:{M}:{S}")
               etiqueta4.after(500,actualizar)
          elif(M>=60):
               H2  , residuo = divmod(M, divisor)
               M2=residuo
               M=0
               print(f"H2:{H2}, M2:{M2},S:{S}") 
               #palabra.set(f"{D}:{H}:{M}:{S}")
               etiqueta4.after(500,actualizar)
          elif(H>=24):
               D2  , residuo = divmod(H, divisorDias)
               H=0
               H2=residuo
               etiqueta4.after(500,actualizar)
          elif(S==60):
               if(M==59):
                  if(H==23):
                    S=0
                    M=0
                    H=0
                    D=D+1
                    palabra.set(f"{D}:{H}:{M}:{S}")
                    etiqueta4.after(500,actualizar)
                  else:
                    S=0
                    M=0
                    H=H+1
                    palabra.set(f"{D}:{H}:{M}:{S}")
                    etiqueta4.after(500,actualizar)
                 
               else:
                 M=M+1
                 S=0
                 palabra.set(f"{D}:{H}:{M}:{S}")
                 etiqueta4.after(500,actualizar)

          else:
           palabra.set(f"{D}:{H}:{M}:{S}")
           etiqueta4.after(500,actualizar)
     #Rparo
     elif(Reloj==0):
          palabra.set(f"{D}:{H}:{M}:{S}")
          etiqueta4.after(1,actualizar) 
     #Rpausa
     elif(Reloj==2):
           cuenta2=cuenta2+1
           palabra.set(f"Cont.. ({D}:{H}:{M}:{S})")
           etiqueta4.after(500,actualizar) 
     #Rborrar      
     elif(Reloj==3):
           cuenta2=0
           S=0
           palabra.set("")
           etiqueta4.after(1,actualizar) 
     else:
       etiqueta4.after(10,actualizar) 
           

def numero(a):
    global Reloj
    global cadena
    global cadena2
    global variableC
    cadena=variableA.get()  
    if (a=="1"):
       cadena+="1"
       variableA.set(cadena)
    elif(a=="2"):
         cadena+="2"
         variableA.set(cadena)
    elif(a=="3"):
         cadena+="3"
         variableA.set(cadena)
    elif(a=="4"):
         cadena+="4"
         variableA.set(cadena)
    elif(a=="5"):
         cadena+="5"
         variableA.set(cadena)
    elif(a=="6"):
         cadena+="6"
         variableA.set(cadena)
    elif(a=="7"):
         cadena+="7"
         variableA.set(cadena)
    elif(a=="8"):
         cadena+="8"
         variableA.set(cadena)
    elif(a=="9"):
         cadena+="9"
         variableA.set(cadena)
     
    elif(a=="0"):
         cadena+="0"
         variableA.set(cadena)
    elif(a=="c"):
         cadena=""
         variableA.set(cadena)
         valorDeA.config(bg="silver") 

    elif((a=="+")or (a=="-")or(a=="*")or(a=="/")):
 #        if(valorDeA.get() !=""):
#              valorDeA.get()=
             
         variableC=a  
         cadena2=variableA.get()
         cadena=""
         variableA.set("")
         
    elif(a=="="):
        if(variableC=="+"):
          sumar()
        elif(variableC=="-"):
             restar()
        elif(variableC=="*"):
             multiplicar()
        elif(variableC=="/"):
             dividir()  

    elif(a=="Ron"):
         Reloj=1
         a=""
    elif(a=="Rparo"):
         Reloj=0
         a=""
    elif(a=="Rpausa"):
         Reloj=2
         a=""
    elif(a=="Rborrar"):
         Reloj=3
         a=""
             
root = Tk()
variableA=StringVar()
variableB=StringVar()
resultado=StringVar()
palabra=StringVar()
relojvariable=StringVar()

etiquetaCalculadora=Label(root)
etiquetaCalculadora.config(bg="lightblue")
etiquetaCalculadora.grid()

etiqueta = Label(etiquetaCalculadora)
etiqueta.config(width=5,height=5)
etiqueta.grid(row=1,column=0)

operaciones=Label(etiquetaCalculadora)
operaciones.config(width=5, height=8,bg="silver")
operaciones.grid(row=1,column=1)

valorDeA=Entry(etiquetaCalculadora ,textvariable=variableA)
valorDeA.config(font=("verdana,15"),bg="silver",width=10,cursor="pencil")
valorDeA.grid(row=0,column=0)

botonSumar = Button(operaciones,text=" + ")
botonSumar.config(command=lambda:numero("+"),cursor="heart",bg="red",fg="white",font=("arial",9),border=3,relief="solid") #command=sumer,
botonSumar.grid(row=0,column=0)

botonRestar = Button(operaciones,text=" - ")
botonRestar.config(command=lambda:numero("-"),cursor="heart",bg="red",fg="white",font=("arial",10),border=3,relief="solid") #command=mostrar
botonRestar.grid(row=1,column=0)


botonMultiplicar= Button(operaciones,text=" * ")
botonMultiplicar.config(command=lambda:numero("*"),cursor="heart",bg="red",fg="white",font=("arial",9),border=4,relief="solid") #command=mostrar
botonMultiplicar.grid(row=2,column=0)


botonDividir= Button(operaciones,text=" / ")
botonDividir.config(command=lambda:numero("/"),cursor="heart",bg="red",fg="white",font=("arial",10),border=3,relief="solid") #command=mostrar
botonDividir.grid(row=3,column=0)

############################################
######## CRONOMETRO ########################
############################################

etiquetaCronometro=Label(root)
etiquetaCronometro.config(bg="lightblue",width=10,height=10)
etiquetaCronometro.grid(row=0,column=1)

etiqueta4= Label(etiquetaCronometro,textvariable=palabra)
etiqueta4.config(border=3,relief="solid",fg="black",width=12,height=1,bg="silver",cursor="exchange")
etiqueta4.grid(row=0,column=0)

etiquetaCbotones=Label(etiquetaCronometro)
etiquetaCbotones.config(bg="lightblue",cursor="hand2")
etiquetaCbotones.grid(row=1,column=0)
botonCronometro= Button(etiquetaCbotones,text="   Empezar   ")
botonCronometro.config(command=lambda:numero("Ron"))
botonCronometro.grid(row=1,column=0)
##########
etiquetaParoGeneral=Label(etiquetaCbotones)
etiquetaParoGeneral.config(bg="lightblue")
etiquetaParoGeneral.grid(row=2)
botonCPausa= Button(etiquetaParoGeneral,text="Pausa")
botonCPausa.config(command=lambda:numero("Rpausa"))
botonCPausa.grid(row=0,column=0)

botonCParo=Button(etiquetaParoGeneral,text="Paro")
botonCParo.config(command=lambda:numero("Rparo"))
botonCParo.grid(row=0,column=1)

botonCborrar=Button(etiquetaCbotones,text="      Borrar      ")
botonCborrar.config(command=lambda:numero("Rborrar"))
botonCborrar.grid(row=3)
labelEspacio=Label(etiquetaCbotones)
labelEspacio.config(width=1,height=6,bg="lightblue")
labelEspacio.grid(row=4)
#############
actualizar()

root.iconbitmap(icon_path) #debe estar en la misma carpeta
#reloj=Label(root,textvariable=palabra)
#########################################################

numero1= Button(etiqueta,text="1")
numero1.config(width=2,height=2,command=lambda:numero("1"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero1.grid(row=1,column=0)
numero2= Button(etiqueta,text="2")
numero2.config(width=2,height=2,command=lambda:numero("2"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero2.grid(row=1,column=1)

numero3= Button(etiqueta,text="3")
numero3.config(width=2,height=2,command=lambda:numero("3"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero3.grid(row=1,column=2)

numero4= Button(etiqueta,text="4")
numero4.config(width=2,height=2,command=lambda:numero("4"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero4.grid(row=2,column=0)

numero5= Button(etiqueta,text="5")
numero5.config(width=2,height=2,command=lambda:numero("5"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero5.grid(row=2,column=1)

numero6= Button(etiqueta,text="6")
numero6.config(width=2,height=2,command=lambda:numero("6"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero6.grid(row=2,column=2)

numero7= Button(etiqueta,text="7")
numero7.config(width=2,height=2,command=lambda:numero("7"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero7.grid(row=3,column=0)

numero8= Button(etiqueta,text="8")
numero8.config(width=2,height=2,command=lambda:numero("8"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero8.grid(row=3,column=1)

numero9= Button(etiqueta,text="9")
numero9.config(width=2,height=2,command=lambda:numero("9"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero9.grid(row=3,column=2)

numero0= Button(etiqueta,text="0")
numero0.config(width=2,height=2,command=lambda:numero("0"),cursor="heart",bg="blue",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
numero0.grid(row=4,column=1)

botonIgual= Button(etiqueta,text=" = ")
botonIgual.config(width=2,height=2,command=lambda:numero("="),cursor="heart",bg="gold",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
botonIgual.grid(row=4,column=2)

botonClear = Button(etiqueta,text=" C ")
botonClear.config(width=2,height=2,command=lambda:numero("c"),cursor="heart",bg="silver",fg="white",font=("arial",9),border=3,relief="solid") #command=mostrar
botonClear.grid(row=4,column=0)
#####################################################
root.config(bg="lightblue",cursor="X_cursor")
root.title("calculadorita")
root.mainloop()


