f = load('dats3.dat');
G = load('dater.dat');
r = 30;
x = f(:,1);
y = f(:,2);
xp = G(:,1);
yp = G(:,2);
xc = 10-x;
tantheta = xc/r;
theta =  atand(tantheta);
DSE = [theta, yp];
DE = [theta, y];
save -ascii 'dse.dat' DSE
save -ascii 'de.dat' DE

#plot (theta, y, theta,  yp)

