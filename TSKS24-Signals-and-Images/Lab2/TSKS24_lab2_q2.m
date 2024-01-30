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

fx1 = fft(x1);       %DFT av x1
fx2 = fft(x2);       %DFT av x2

hold on
%plot(f, abs(fx1));
%axis([0.799e4 0.804e4 0 5e4]);
%plot(f, abs(fx2));
plot(f, db(abs(fx1)));
plot(f, db(abs(fx2)));
