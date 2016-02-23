f= load('datos/dat.dat');
  f1=sum(f())
  f2=f1/140
save -ascii 'datos/prom.dat' f2
