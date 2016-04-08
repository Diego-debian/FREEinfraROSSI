x = [0.01,0.002,0.6]
z1 = size(x)
axis([0, 0.6, 0, 0.0200])
title('Distancia vs Intensidad \n')
xlabel('Distancia [m]')
ylabel('Intensidad [W]')
I0= 0.000259*(x.^(-2))
I1= 0.000045*(x.^(-2))
I2= 0.000043*(x.^(-2))
I3 = 0.000042*(x.^(-2))
I4 = 0.000034*(x.^(-2))
I5 = 0.000047*(x.^(-2))
plot (x, I0, x, I1, x, I2, x, I3, x, I4, x, I5)
pause
