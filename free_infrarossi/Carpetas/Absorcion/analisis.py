#/usr/bin/python
#!*-* coding:utf-8 *-*
import numpy as np
import os
import serial
import subprocess
import math
import time
import Gnuplot
import shutil
import matplotlib.pylab as pl

x = [0.001,0.002,0.6]
z1 = np.size(x)
pl.axis([0, 0.6, 0, 0.02])
pl.title('Distancia vs Intensidad \n')
pl.xlabel('Distancia [m]')
pl.ylabel('Intensidad [W]')
Io= 0.000259*(x**(-2))
I1= 0.000045*(x**(-2))
I2=0.000043*(x**(-2))
I3 = 0.000042*(x**(-2))
I4 = 0.000034*(x**(-2))
I5 = 0.000047*(x**(-2))

