#!/bin/python
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
class estadis:
    def Llamar(self):
	os.system("octave est_fuente.m")
	
    def Estadis(self):
	self.x , self.y = np.loadtxt('de.dat', unpack=True,  usecols=[0,1])
	self.xp , self.yp = np.loadtxt('dse.dat', unpack=True,  usecols=[0,1])
	print self.x, self.y

    def Graf0(self):
	pl.subplot(221)
	pl.xlabel('ANGULO [grados]')
	pl.ylabel('Intensidad [micro W]')
        pl.title('DISPERSION SIN SISTEMA OPTICO\n')
	pl.grid()
	pl.plot(self.xp, self.yp, 'o--')
    
    def Graf1(self):
	pl.subplot(222)
	pl.xlabel('ANGULO [grados]')
	pl.ylabel('Intensidad [micro W]')
        pl.title('DISPERSION CON SISTEMA OPTICO\n')
	pl.grid()
	pl.plot(self.x, self.y, 'R')

    def Graf2(self):
	pl.subplot(212)
	pl.xlabel('ANGULO [grados]')
	pl.ylabel('Intensidad [micro W]')
        pl.title('DISPERSION SIN Y CON SISTEMA OPTICO\n')
	pl.grid()
	pl.plot(self.x, self.y, 'R')
	pl.plot(self.xp, self.yp, 'o--')

    def Plotear(self):
        pl.subplots_adjust(left=0.11)
        pl.subplots_adjust(bottom=0.13)
	pl.subplots_adjust(right=0.90)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.56)
        pl.subplots_adjust(hspace=0.71)
        pl.savefig('Graficas.png')
        pl.show()
	

    def __init__(self):
	self.Llamar()
	self.Estadis()
	self.Graf0()
	self.Graf1()
	self.Graf2()
	self.Plotear()
esto = estadis()
