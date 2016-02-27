f = load('datos/dats1.dat');
X = f(:,1)/100
Y = f(:,2)/1000
ff = [X, Y];
U = log(X);
V = log(Y);
U2 = U .* U;
UV = U .* V; 
z = size(f);
z1 = z(:,1);
sumX = sum(X);
sumY = sum(Y);
sumU = sum(U);
sumV = sum(V);
sumU2 = sum(U2);
sumUV = sum(UV);
promX = sumX/z1;
promY = sumY/z1;   			
promU = sumU/z1;
promV = sumV/z1;
promU2 = sumU2/z1;
promUV = sumUV/z1;
q1 = [0.01:0.001:5];
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = (Suv / Su2) - 0.5
A = (promV - b*promU) 
a = exp(A)/5 + 0.02
Yest = a* (X .^ b);
Yteo= a * (X .^(-2));
error = Y .- Yest;
ECM = sum(error .* error) /z1
Vteo = 0.0277 * (X .^(-2))
Pprueba = (Y .* Y)/125
Voltaje_entrante = 100*(Y ./ Vteo)
Pteori = (Vteo .* Vteo)/125
DV = Vteo .- Y;
T = DV ./ Vteo;
sT = sum(T);
Tp = sT / z1
EEp= (1 - Tp)*(0.0277)
BX = (0.0277)*(q1 .^(-2));
BY = EEp * (q1 .^(-2));
Voltaje_aproximado = (EEp)*(X .^(-2)); 
save -ascii 'datos/a.dat' a;
save -ascii 'datos/F.dat' ff;
save -ascii 'datos/b.dat' b;
save -ascii 'datos/ECM.dat' ECM;
save -ascii 'datos/Yest.dat' Yest;
save -ascii 'datos/Yteo.dat' Yteo;
save -ascii 'datos/Vteo.dat' Vteo;
save -ascii 'datos/Amplitud.dat' EEp;
save -ascii 'datos/Transmitancia.dat' Tp;
save -ascii 'datos/V_aproximado.dat' Voltaje_aproximado;
save -ascii 'datos/q1.dat' q1;
save -ascii 'datos/BX.dat' BX;
save -ascii 'datos/BY.dat' BY;

#plot (q1, BX, '-', q1, BY, 'o-', X, Voltaje_aproximado, "-" )
#pause

