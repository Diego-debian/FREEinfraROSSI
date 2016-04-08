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
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.


f = load('datos/dats1.dat'); #-------------entrada de datos a través del archivo .dat
X = f(:,1)/100 #-----------datos de distancia en metros
Y = f(:,2)/1000000 #-----------datos de voltaje  en voltios
ff = [X, Y]; # ---------------voltaje como funcion X e Y
U = log(X); # ----------------logaritmo natural de la distancia
V = log(Y); #---------------- logaritmo natural del voltaje
U2 = U .* U; #-------------------- el cuadrado del logarito de la distancia
UV = U .* V; # ......................logaritmo del producto del voltaje y la distancia
z = size(f); #----------------------- tamaño de filas y columnas del archivo .dat
z1 = z(:,1); #----------------------- tamaño de columnas del archivo .dat
sumX = sum(X); # --------------------- sumatoria de todos los datos de la distancia en metros
sumY = sum(Y); # --------------------- sumatoria de todos los datos del voltaje en voltios
sumU = sum(U); # --------------------- sumatoria de todos los datos del logaritmo de la distancia 
sumV = sum(V); # --------------------- sumatoria de todos los datos del logaritmo del voltaje 
sumU2 = sum(U2); # --------------------- sumatoria de todos los datos del cuadrado del logaritmo de la distancia 
sumUV = sum(UV);  # --------------------- sumatoria de todos los datos del producto de el logaritmo del voltaje y la distancia
promX = sumX/z1;  # --------------------- el promedio de la distancia
promY = sumY/z1;  # --------------------- el promedio del voltaje 			
promU = sumU/z1; # --------------------- promedio del logaritmo de la distancia
promV = sumV/z1; # --------------------- promedio del logaritmo del voltaje
promU2 = sumU2/z1; # --------------------- promedio del logaritmo la distancia
promUV = sumUV/z1; # --------------------- promedio del cociente del logaritmo de la distancia y el voltaje.
#------------------------------Primer calculo-----------------------------
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
#b = (Suv / Su2) - 0.5
b = (Suv / Su2)
A = (promV - b*promU) 
#a = exp(A)/5 + 0.02
a = exp(A)
Yest = a* (X .^ b);
Yteo= a * (X .^(-2));
error = Y .- Yest;
ECM = sum(error .^(2)) /z1
save -ascii 'datos/a.dat' a;
save -ascii 'datos/F.dat' ff;
save -ascii 'datos/b.dat' b;
save -ascii 'datos/ECM.dat' ECM;
save -ascii 'datos/Yest.dat' Yest;
#------------------------------segundo calculo-----------------------------
Vteo = 0.000259 * (X .^(-2))
q1 = [0.01:0.001:5];
Pprueba = (Y .* Y)/125 #---------- Potencia en el diodo
Voltaje_entrante = 100*(Y ./ Vteo)
Pteori = (Vteo .* Vteo)/125
DV = Vteo .- Y;
T = DV ./ Vteo;
sT = sum(T);
Tp = sT / z1;
Trasmitancia = Tp
Reflectancia = 1 - Tp
EEp= (Reflectancia)*(0.000259);
densidad_voltaje = EEp
Voltaje_aproximado = (EEp)*(X .^(-2)); 
BX = (0.000259)*(q1 .^(-2));
BY = EEp * (q1 .^(-2));
V_estimado = EEp*(X .^(-2));
error1 = Y .- V_estimado;
ECM1 = sum(error1 .^(2)/z1)
save -ascii 'datos/Yteo.dat' Yteo;
save -ascii 'datos/Vteo.dat' Vteo;
save -ascii 'datos/Amplitud.dat' EEp;
save -ascii 'datos/Transmitancia.dat' Tp;
save -ascii 'datos/V_aproximado.dat' Voltaje_aproximado;
save -ascii 'datos/q1.dat' q1;
save -ascii 'datos/BX.dat' BX;
save -ascii 'datos/BY.dat' BY;
save -ascii 'datos/ECM1.dat' ECM1;

#plot (q1, BX, '-', q1, BY, 'o-', X, Voltaje_aproximado, "-" )
#pause

