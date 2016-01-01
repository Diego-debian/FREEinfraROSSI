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
        # MAXIMO n en el for 130
        # Distancia de separacion 24 cm
	# Distancia de recoleccion 22,5 cm
	#Paso en centimetros pausada 1 = 0,34
        #Paso en centimetros pausada 2 = 0,30
        #Paso en centimetros pausada 3 = 0,27
        #Paso en centimetros pausada 4 = 0,213
        #Paso en centimetros pausada 5 = 0.17
        for n in range (0, 117): 
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
            arduino.write('zz')
            for i in range(0, 140):
                arduino=serial.Serial(self.puerta, 9600)
                archi = open('datos/dat.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = 0.205*2*(132 - n)
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
	os.system("octave bin/estadistica.m")
	f = np.loadtxt("datos/dats1.dat")
	a = np.loadtxt("datos/a.dat")
	A = np.loadtxt("datos/A.dat")
	self.X = f[:,0]
	self.V = f[:,1]
	self.x1 = self.X/100
	self.v1 = self.V/1000
	self.F = [self.x1, self.v1]
	self.a1 = round(float(a),4)
#	A2 = A/10
	self.A1 = round(float(A),2)
#	self.x = np.arange(0,0.6, 0.00563)
	self.x = np.arange(0.01,0.6, 0.00507)
	self.y = (((self.a1)*(self.x)**(self.A1)))
	self.yz = (((self.a1)*(self.x)**(-2)))
#	self.Y2= self.y
	self.Y2 = self.v1-self.y
	self.VAR = pow(pow(self.Y2,2) , 0.5)
	self.sum = round(np.sum(self.VAR, axis=0)/118 , 4)
	self.yf = self.y #+ self.sum
	self.tam = int(self.y.size)	
	print self.x1, self.v1,"\n\n\n", self.a1," X^(",self.A1,") + ", self.sum , "\n\n\n", self.tam

    def Grafica(self):
	pl.subplot(221)
        #time.sleep(10)
        pl.title('Distancia vs Voltaje \n')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
	pl.plot(self.x1, self.v1, 'g:x')
        pl.plot(self.x, self.yf, 'W')
	pl.axis([0, 0.6, -0.001, 5])
        pl.text(0.2, 4, r'Datos recolectados')
#	pl.show()


    def Grafica1(self):
        pl.subplots_adjust(right=0.97)
        pl.subplots_adjust(left=0.1)
        pl.subplots_adjust(bottom=0.13)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.24)
        pl.subplots_adjust(hspace=0.60)
	

    def Grafica2(self):
	pl.subplot(222)
        pl.title('APROXIMACION')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
        pl.plot(self.x, self.yf, 'B')
        pl.plot(self.x, self.yz, 'R')
	pl.axis([0, 0.6, -0.001, 5])
#	self.a1," X^(",self.A1,") + ", self.sum
        pl.text(0.35, 4, r'Azul')
        pl.text(0.25, 3.5, r'' + str(self.a1) + '*X^('+ str(self.A1)+')')
        pl.text(0.35, 2, r'Rojo')
        pl.text(0.33, 1.5, r'' + str(self.a1) + '*X^(-2)')
        
    def Grafica3(self):
        pl.subplot(212)
	pl.plot(self.x1, self.v1, 'g:o')
        pl.plot(self.x, self.yf, 'B')
        pl.plot(self.x, self.yz, 'R')
        pl.subplot(212)
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
        pl.title('Distancia vs Voltaje \n')
        pl.legend(loc='upper left')
	pl.axis([0, 0.6, -0.001, 5])
	pl.text(0.4, 4, r'Azul V=' + str(self.a1) + '*X^('+ str(self.A1)+')')
        pl.text(0.4, 3, r'Rojo V=' + str(self.a1) + '*X^(-2)')
        pl.savefig('datos/Atenuacion.png')
        pl.show()
	
    def Ordenar(self):
	os.system("python bin/o_Carpetas.py")


                
    def __init__(self):
	self.Verifica()
        self.Comenzar()
	self.Analisis()
	self.Grafica()
	self.Grafica1()
	self.Grafica2()
	self.Grafica3()
	self.Ordenar()
        self.__del__()
            
    def __del__(self):
        print ("PROGRAMA TERMINADO")
                
                
Iniciar  = App()
