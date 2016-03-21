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
import numpy as np
import os
import serial
import subprocess
import math
import time
import Gnuplot
import shutil
import matplotlib.pylab as pl
class App:  
    def Verifica(self):
	os.system('rfcomm  -a  > conexion.txt | cut -d ":" -f 1,1  conexion.txt > direccion.txt ')
	puerto = open('direccion.txt', 'r')
	self.puerto = puerto.read(7)
	puerto.close()
	self.puerta = "/dev/"+self.puerto
	print self.puerta
        try:       
            arduino = serial.Serial(self.puerta, 9600)
            arduino.write("aa")
  	except:
	    os.system("exit")

    def Salir(self):
        exit() 

    def Comenzar(self):
        # Distancia de separacion 28 cm
	# Distancia de recoleccion 25 cm
	#Paso en centimetros pausada 1 = 0,34
        #Paso en centimetros pausada 2 = 0,30
        #Paso en centimetros pausada 3 = 0,27
        #Paso en centimetros pausada 4 = 0,245
        #Paso en centimetros pausada 5 = 0.213
        for n in range (0, 117): 
            os.system('rm datos/dat.dat')
            #time.sleep(2)
            arduino= serial.Serial(self.puerta, 9600)
	    print "aca va la lectura"
            arduino.write("aa")
            #time.sleep(1)
            arduino.write('4')
            arduino.close()
            arduino=serial.Serial(self.puerta, 9600)
            time.sleep(2)
            arduino.write('zz')
            for i in range(0, 140):
                arduino=serial.Serial(self.puerta, 9600)
                archi = open('datos/dat.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = 0.21367*2*(140 - n)
                xo = str(z)
                yo = str(x)
                print "paso numero", n
                print "(cm) \t (microW)"
                print('{0} {1}').format(xo, yo)
                archi.write (xo)
                archi.write (" ")
                archi.write (yo)
                archi.close()  
            else:
		os.system("octave bin/prom1.m")
		archi = open('datos/prom.dat', 'a+')
                print("aca va la pausa")
                Lectura = archi.read()
                archi.close() 
                archi1 = open('datos/dats1.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                arduino.write('aa')
                arduino.close()

    def Analisis(self):
#	os.system("python bin/Estadistica2.py")
	os.system("python bin/estadis2.py")
	time.sleep(3)
	
	
    def Ordenar(self):
	os.system("python bin/o_Carpetas1.py")


                
    def __init__(self):
	self.Verifica()
        self.Comenzar()
	self.Analisis()
        self.__del__()
            
    def __del__(self):
        print ("PROGRAMA TERMINADO")
                
                
Iniciar  = App()
