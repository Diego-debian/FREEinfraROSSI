f= load('datos/dat.dat');
  f1=sum(f())
  z = size(f); #----------------------- tamaño de filas y columnas del archivo .dat
  z1 = z(:,1); #----------------------- tamaño de columnas del archivo .dat
  f2 = f1/z1
save -ascii 'datos/prom.dat' f2
