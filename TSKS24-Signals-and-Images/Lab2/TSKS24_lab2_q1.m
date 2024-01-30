%Input data for two (x1, x2) signals

T=2.5;              %Tidsutbredning
fs=4e4;             %Samplingfrekvens
N=T*fs;             %Antal Sampel
n=0:N-1;            %Vektor med sampelindex
t=1/fs*n;           %Vektor med sampeltidpunkter
f1=8000;            %Signalens frekvens för f1
x1=sin(2*pi*f1*t);  %Vektor med alla sampel för x1
f2=8017;            %Signalens frekvens för f2
x2=sin(2*pi*f2*t);  %Vektor med alla sampel för x2



