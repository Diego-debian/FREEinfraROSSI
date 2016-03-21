#/usr/bin/python
#!*-* coding:utf-8 *-* 
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad  Distrital Francisco Jose  
# Grupo de fisica e informatica
# Diego Alberto Parra Garzón 
# Dr Julian Andres Salamanca Bernal
# Colombia, Bogota D.C.
import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox
import Tkinter
import shutil

class Gramo():
    def Atenua(self):
        bicho = Tk()
        bicho.geometry("280x170+200+90")
        bicho.config(bg="white")
        bicho.title("Infrarossi")
        bicho.resizable(width=0, height=0)
      
        def Verifica():
	    print "ola"

	def Salir():
            tkMessageBox.showinfo("Infrarossi", message= "Saliendo .... ")
	    arduino = serial.Serial("/dev/rfcomm0", 9600)
	    arduino.write('aa')
	    exit()
	    exit()

	def Grafica():
	    os.system("python g_p_Ate.py &")

	def Comenzar1():
            tkMessageBox.showinfo("Infrarossi", message= "Se procede a capturar datos, para detener el proceso cierre la ventana de captura de datos 'de color azul'")
	    os.system("xterm -T Infrarossi -geom 50x8+185+100 +cm -bg blue -e python bin/c_p_Ate.py &")
	   # os.system("python bin/c_p_Ate.py")

# --------------------------------CONFIGURACION DE VENTANA ------------------------------------------------------------------------------
        X=8
	Y=10
	lblTitulo = Label(bicho, text="ATENUACION", fg = ("blue"), bg = ("white"), font = ("Century Schoolbook L",23)).place(x=30, y=20)
        btnConectar1 = Button(bicho, text= " INICIAR ", width=5, height=1, command= Comenzar1).place(x=20+X, y=100+Y)               
        btnSalir = Button(bicho, text= " SALIR ", width=5, height=1, command= Salir).place(x=170+X, y=100+Y)    
        btnGrafica = Button(bicho, text= " GRAFICA ", width=5, height=1, command= Grafica).place(x=95+X, y=100+Y)    
	Verifica()       
        bicho.mainloop()  	

    
    def __init__(self):
        self.Atenua()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()
