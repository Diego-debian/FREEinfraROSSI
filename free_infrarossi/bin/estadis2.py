#!/usr/bin/python
#-*- coding:utf-8 -*-
from matplotlib.widgets import  RectangleSelector
from numpy import *
import numpy as np
import matplotlib.pyplot as pl
import os
import subprocess
import math
import time
import shutil
import Gnuplot
from matplotlib.widgets import Cursor
from pylab import *
class Estadistica:
    def Cargar(self):
#	self.f= np.loadtxt('datos/dats1.dat')
	self.x , self.y = np.loadtxt('datos/dats1.dat', unpack=True,  usecols=[0,1])
#	self.x , self.y = np.loadtxt('dats1.dat', unpack=True,  usecols=[0,1])
	self.n = np.size(self.x)
	self.k = np.ceil(1 + np.log2(self.n)) # comando ceil redondea el numero al mayor entero
	self.c = np.sort(self.y) #comando sort guarda los datos de y
	self.lon = self.c[110]/8
	
	print "El tamaño de la muestra es: ", self.n , "\nEl tamaño del intervalo es ", self.k, self.lon

    def Grafica(self):
	def onselect(eclick, erelease):
	    print(' startposition : (%f, %f)' % (eclick.xdata, eclick.ydata))
	    print(' endposition   : (%f, %f)' % (erelease.xdata, erelease.ydata))
	    print(' used button   : ', eclick.button)  
	    self.xinicial = round(eclick.xdata,2)
	    self.yinicial= round(eclick.ydata,2)
	    self.xfinal = round(erelease.xdata,2)
	    self.yfinal = round(erelease.ydata,2)
	    print self.xinicial, self.yinicial , self.xfinal, self.yfinal

	def toggle_selector(event):
	    print(' Key pressed.')
	    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        	print(' RectangleSelector deactivated.')
	        toggle_selector.RS.set_active(False)
	    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
	        print(' RectangleSelector activated.')
	        toggle_selector.RS.set_active(True)

	pl.xlabel('Distancia [m]')
	pl.ylabel('Voltaje [V]')
        pl.title('LONGITUD DE ONDA DIODO INFRARROJO \n')
	fig = figure
	ax = subplot(111)
  #      pl.legend(loc='upper left')
        ax.plot(self.x, self.y, 'o--')
	cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
	toggle_selector.RS = RectangleSelector(ax, onselect, drawtype='line')
	connect('key_press_event', toggle_selector)
	pl.show()

    def Estadistica(self):
	self.distancia = self.xfinal - self.xinicial
	d = 4.81*10**(-6)
	x = self.distancia*10**(-2)
	y = 45*10**(-2)
	tetharad = math.atan(x/y)
	tethagra = math.degrees(tetharad)
	sintetha= math.sin(tetharad)
	self.lamda = round((2*d*sintetha)*10**(9),2)
	self.error = round(pow(pow(800-self.lamda,2),0.5), 2)
	self.error1 = round(pow(pow(100-self.lamda*100/800, 2), 0.5), 3)
	print tethagra, "\n ", sintetha
	print "la longitud de onda aproximada para el diodo infrarrojo es",  self.lamda	, "nanometros, con un error de ", self.error1 , " %" 

    def Grafica1(self):
	self.x1 = self.x/100
	self.y1 = self.y /1000
	pl.subplot(221)
	pl.plot(self.x1,self.y1, 'o--')
	pl.title('Datos Capturados  \n')
	pl.xlabel('Distancia [m]')
	pl.ylabel('Voltaje [V]')
#	pl.ylim(0, 0.02) 

    def Grafica2(self):
	pl.subplot(222)
        pl.plot(self.x1, self.y1, 'o--')
        pl.title('Patrones de Interferencia \n')
 	pl.xlabel('Distancia [m]')
	pl.ylabel('Voltaje [V]')
	pl.text(0.06, 0.02, r' x1 = ' + str(self.xinicial/100))
	pl.text(0.06, 0.018, r' x2 = ' + str(self.xfinal/100))
	pl.text(0.06	, 0.016, r' x2-x1 = ' + str(self.distancia/100))
# 	pl.ylim(0, 0.036) 
        pl.plot([self.xinicial/100, self.xinicial/100], [0, 0.015], '-')
        pl.plot([self.xfinal/100, self.xfinal/100], [0, 0.015], '-')
        pl.plot(self.x1, self.y1, 'o--')
	pl.ylim(0, 0.022) 

    def Grafica3(self):
	pl.subplot(212)
        pl.plot(self.x1, self.y1, 'o--')
        pl.plot([self.xinicial/100, self.xinicial/100], [0, 0.015], '-')
        pl.plot([self.xfinal/100, self.xfinal/100], [0, 0.015], '-')
#        pl.plot([self.xinicial/100, self.xfinal/100], [0.013, 0.013], '-')
	pl.text(0.04, 0.016, r' distancia entre asintotas '+str(self.distancia/100) + '[m] ')
	pl.text(0.04, 0.020, r' m:1 Lamda IRE =' +  str(self.lamda) + ' [nm}      +/- ' + str(self.error) + ' [nm]')
	pl.text(0.04, 0.018, r' Error porcentual  ' + str(self.error1) + ' %')
 	pl.ylim(0, 0.022) 
	pl.xlabel('Distancia [m]')
	pl.ylabel('Voltaje [V]')
        pl.title('LONGITUD DE ONDA DIODO INFRARROJO \n')

    def Plotear(self):
	pl.subplots_adjust(right=0.97)
        pl.subplots_adjust(left=0.11)
        pl.subplots_adjust(bottom=0.13)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.32)
        pl.subplots_adjust(hspace=0.71)
        pl.savefig('datos/Graficas.png')
        pl.show()

    def ordena(self):
	os.system("python bin/o_Carpetas1.py")
    
    def __init__(self):
	self.Cargar()
	self.Grafica()
	self.Estadistica()
	self.Grafica1()
	self.Grafica2()
	self.Grafica3()
	self.Plotear()
#	self.ordena()

esto = Estadistica()
