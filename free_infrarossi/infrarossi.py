#!/usr/bin/python
# *-* coding:utf-8 *-*
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad Distrital Francisco Jose  
# Grupo de fisica e informatica
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.

import numpy as np
import pylab as pl
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

class App:
    def Modulo(self):
        bicho = Tk()
        bicho.geometry("430x180+180+60")
        bicho.config(bg="white")
        bicho.title("Infrarossi")
        bicho.resizable(width=0, height=0)
           
        def Salir():
	    tkMessageBox.showinfo("Infrarossi", message= "! Cerrando el programa ¡")
	    os.system("rm MAC.txt MACD.txt puerto.txt conexion.txt direccion.txt dispo.txt log.txt mac.txt macd.txt texput.log x.log")
	    os.system("rm MAC.txt MACD.txt puerto.txt")
	    os.system("sh bin/d_Blu.sh &")
            exit()


        def Verifica():
	    tkMessageBox.showinfo("Infrarossi", message= "! Conectando con el dispositivo, por favor espere ¡")
            os.system('xterm -T Infrarossi -geom 50x8+185+100 +cm -bg blue -e sh c_Blu.sh ')
	    Conecta()
	    
	def Conecta():
            os.system('rfcomm  -a  > conexion.txt | cut -d ":" -f 1,1  conexion.txt > direccion.txt ')
	    puerto = open('direccion.txt', 'r')
	    self.puerto = puerto.read(7)
	    puerto.close()
	    self.puerta = "/dev/"+self.puerto
	    print self.puerta

	    Conectar()

	def Conectar():
            tkMessageBox.showinfo("Infrarossi", message= "! Verificando conexion ¡")
	    print self.puerta
	    try:
		arduino = serial.Serial(self.puerta, 9600)
		time.sleep(4)
                arduino.write("aa")
                Valido()
                Valido()
	    except:
                tkMessageBox.showinfo("Infrarossi", message= "! No hay conexion ¡")
               # os.system('xterm -T Infrarossi -geom 50x8+185+100 +cm -bg blue -e sh c_Blu.sh &')
	
        
        def Valido():
# ................. Botones menu de inicio ....................................
	    x1 = int(150)
	    y3 = int(300)
            lblRapidez = Label(bicho, text="\nMENU\nDE INICIO", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=15+x1, y=280-y3)
            btnComenzar = Button(bicho, text= "Difraccción", width=6, height=1, command= Difraccion).place(x=20+x1, y=350-y3)
            btnDetener= Button(bicho, text= "Atenuación", width=6, height=1, command= Atenuacion).place(x=20+x1, y=380-y3)
	    btnLimpiar = Button(bicho, text= "Absorción", width=6, height=1, command= Absorcion).place(x=20+x1, y=410-y3) 	 



#------------------------------------- Funcion limpiar pantalla ---------------------------------------------------
        def Reset():
	    tkMessageBox.showinfo("Infrarrosi", message= "! Limpiando, por favor espere ¡")
	    os.system("rm MAC.txt MACD.txt puerto.txt conexion.txt direccion.txt")
	    os.system("sh bin/d_Blu.sh &")
	    os.system("python infrarossi.py &")
	    os.system("rm MAC.txt MACD.txt puerto.txt")
	    exit()

#---------------------------------- Funciones menu           -----------------------------------------------------
        def Difraccion():
	    tkMessageBox.showinfo("Infrarossi", message= "Espere por favor,  Preparando todo para empezar con el experimento.")
	    os.system("python bin/Difraccion.py &")
#	    os.system("xterm -T Infrarrosi -geom 50x8+185+100 +cm -bg blue -e python  bin/Atenuacion.py & ")

	def Atenuacion():
	    tkMessageBox.showinfo("Infrarossi", message= "Espere por favor,  Preparando todo para empezar con el experimento.")
	    os.system("python bin/Atenuacion.py &")
#	    os.system("xterm -T Infrarossi -geom 50x8+185+100 +cm -bg blue -e python  bin/Atenuacion.py & ")

	def Absorcion():
	    tkMessageBox.showinfo("Infrarossi", message= "Para detener la visualización de datos, cierre la ventana de datos 'color azul' u oprima el botón reset del Dispositio ")


#---------------------------------- Bluetooth desconectado ----------------------------
	def Bl_off():
	    tkMessageBox.showinfo("Infrarossi", message= "!Bluetooth desconectado¡")
	    os.system("rm MAC.txt MACD.txt puerto.txt conexion.txt direccion.txt")
	    os.system("sh bin/d_Blu.sh &")
	    os.system("python infrarossi.py &")
	    os.system("rm MAC.txt MACD.txt puerto.txt")
	    exit()
	

# ------------------------------ Definiendo Funcion firmware -----------------------------
	
	def Firmware():
	    tkMessageBox.showinfo("Infrarossi", message= "Conecte la tarjeta microcontroladora arduino uno, con un microcontrolador listo para su uso.\n\nProcediendo con el instalador del firmware")
	    os.system("python bin/firmware/G_firmware.py &")

#--------------------------------Definiendo función Documentación---------------------------------------
	def Documentacion():
            tkMessageBox.showinfo("Infrarossi", message= "! Abriendo documentación, tenga pasciencia ¡")
	    os.system("xdg-open 'Montaje/Articulo_montaje_infrarossi.pdf' &")


#---------------------- Botones Presentacion -----------------------------------------------------------    	
#	yn = int(-210)
#	imgBoton2=PhotoImage(file="Imagenes/cap8.gif")
#        btnLogo= Label(bicho, image=imgBoton2,  height=150, width =180).place(x=150, y=215+yn)

#        lblFisinfor = Label(bicho, text=" GRUPO DE FISICA E INFORMATICA ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=100, y=371+yn)
#	lblInfo = Label(bicho, text="Dr. Julian Andres Salamanca \n Diego Alberto Parra Garzón", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=136, y=390+yn)


#---------------------- Botones Bluetooth -----------------------------------------------------------
	y1 = int(300)
        lblBlue = Label(bicho, text="BLUETOOTH ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=10, y=320-y1)
        btnConectar= Button(bicho, text= " ON ", width=5, height=1, command= Verifica).place(x=20, y=350-y1)
#        btnConectar= Button(bicho, text= " ON ", width=5, height=1, command= Valido).place(x=20, y=350-y1)                        
        btnDesconectar= Button(bicho, text= " OFF ", width=5, height=1, command= Bl_off).place(x=20, y=380-y1) 
	btnSalir=Button(bicho, text = "Salir", command=Salir, height=1, width =5).place(x=20, y=410-y1)


#---------------------- Botones firmware -----------------------------------
	y2 = int(270)
	btnfirmware=Button(bicho, text = "Firmware", command=Firmware, height=1, width =5).place(x=340, y=380-y2)
	btnDocumentacion=Button(bicho, text = "Ayuda", command=Documentacion, height=1, width =5).place(x=340, y=350-y2)
        btnLimpiar = Button(bicho, text= "limpiar", width=5, height=1, command= Reset).place(x=340, y=320-y2) 	 
        bicho.mainloop()  

   
    def __init__(self):
        self.Modulo()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")

if __name__ == "__main__":
    App()

