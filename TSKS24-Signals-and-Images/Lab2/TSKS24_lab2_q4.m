%Input data for two (x1, x2) signals

clear               %clearing the workspace so no mistakes are made

T=2.5;              %Tidsutbredning
fs=4e4;             %Samplingfrekvens
N=T*fs;             %Antal Sampel
n=0:N-1;            %Vektor med sampelindex
t=1/fs*n;           %Vektor med sampeltidpunkter
f1=8000;            %Signalens frekvens för f1
x1=sin(2*pi*f1*t);  %Vektor med alla sampel för x1
f2=8017;            %Signalens frekvens för f2
x2=sin(2*pi*f2*t);  %Vektor med alla sampel för x2
f = fs/N*n;         %Vektor med naturliga frekvensvärden

x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)...
    +1e-3*sin(2*pi*4400*t);

M=500;
w=[zeros(1,floor((N-M)/2)),rectwin(M)',zeros(1,ceil((N-M)/2))];
v=[zeros(1,floor((N-M)/2)),nuttallwin(M)',zeros(1,ceil((N-M)/2))];
y=x.*w;
y2=x.*v;

hold ON;
plot(db(abs(fft(y))));
plot(db(abs(fft(y2))));

M=2000;
w=[zeros(1,floor((N-M)/2)),rectwin(M)',zeros(1,ceil((N-M)/2))];
v=[zeros(1,floor((N-M)/2)),nuttallwin(M)',zeros(1,ceil((N-M)/2))];
y=x.*w;
y2=x.*v;
plot(db(abs(fft(y))));
plot(db(abs(fft(y2))));

plot(db(abs(fft(x))));

legend('M=500 rect', "M=500, Nut", 'M=2000 rect', "M=2000, Nut", "original")


