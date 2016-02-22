f = load('datos/dats1.dat');
X = f(:,1)/100
Y = f(:,2)/1000
ff = [X, Y];
U = log(X);
V = log(Y);
U2 = U .* U;
UV = U .* V; 
sumX = sum(X);
sumY = sum(Y);
sumU = sum(U);
sumV = sum(V);
sumU2 = sum(U2);
sumUV = sum(UV);
promX = sumX/117;
promY = sumY/117;   			
promU = sumU/117;
promV = sumV/117;
promU2 = sumU2/117;
promUV = sumUV/117;
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = (Suv / Su2) - 0.5
A = (promV - b*promU) 
a = exp(A)/5 + 0.02
Yest = a* (X .^ b);
Yteo= a * (X .^(-2));
error = Y .- Yest;
ECM = sum(error .* error) /117
save -ascii 'datos/a.dat' a;
save -ascii 'datos/F.dat' ff;
save -ascii 'datos/b.dat' b;
save -ascii 'datos/ECM.dat' ECM;
save -ascii 'datos/Yest.dat' Yest;
save -ascii 'datos/Yteo.dat' Yteo;
#plot (X, Y , 'o', X, Yest, '--' )
#pause

