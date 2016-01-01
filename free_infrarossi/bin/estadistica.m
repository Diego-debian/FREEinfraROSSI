f = load('datos/dats1.dat')
X = f(:,1)/100;
Y = f(:,2)/1000;
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
promX = sumX/118;
promY = sumY/118;   			
promU = sumU/118;
promV = sumV/118;
promU2 = sumU2/118;
promUV = sumUV/118;
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = (Suv / Su2)
A = (promV - b*promU) +  0.3
a = exp(A)/5
save -ascii 'datos/a.dat' a;
save -ascii 'datos/A.dat' A;
save -ascii 'datos/F.dat' ff;
