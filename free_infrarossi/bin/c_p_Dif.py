#!/usr/bin/python
# -*- coding:utf-8 -*-
#Creado por Diego Alberto Parra Garzón
#Bogotá - Colombia 

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
        # MAXIMO 130
        # Distancia de separacion a la rejilla de difracción 40 cm
	# Distancia de recoleccion de datos 20 cm
	#Paso en centimetros pausada 1 = 0,34
        #Paso en centimetros pausada 2 = 0,30
        #Paso en centimetros pausada 3 = 0,27
        #Paso en centimetros pausada 4 = 0,24 a 19 Celcius, pausada 4 = 0,180 a 10 Celcius
        #Paso en centimetros pausada 5 = 0,18
        for n in range (0, 111): 
            os.system('rm datos/dat.dat')
            #time.sleep(2)
            arduino= serial.Serial(self.puerta, 9600)
	    print "aca va la lectura"
            arduino.write("aa")
            #time.sleep(1)
            arduino.write('5')
            arduino.close()
            arduino=serial.Serial(self.puerta, 9600)
            time.sleep(2)
            arduino.write('hh')
            for i in range(0, 140):
                arduino=serial.Serial(self.puerta, 9600)
                archi = open('datos/dat.dat', 'a+')
                time.sleep(0.000005)
                x = arduino.readline()
                z = 0.18*n
                xo = str(z)
                yo = str(x)
                print "paso numero", n
                print "(cm) \t (mV)"
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
                # os.system("gnuplot  Datos_C/dat1/agraf.gnp &")
                arduino.write('aa')
                arduino.close()

    def Analisis(self):
	os.system("python bin/Estadistica2.py")
	time.sleep(3)
	
	
    def Ordenar(self):
	os.system("python bin/o_Carpetas.py")


                
    def __init__(self):
	self.Verifica()
        self.Comenzar()
	self.Analisis()
        self.__del__()
            
    def __del__(self):
        print ("PROGRAMA TERMINADO")
                
                
Iniciar  = App()