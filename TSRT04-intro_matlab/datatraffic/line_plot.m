clear;
close all;
load datatraffic;

%Use to plot traffic as a function of time
plot(years, traffic);
xlabel('Year');
ylabel('Data');
title('Data traffic');
legend('Video', 'File transfer', 'Web and other');

%Video dominates the traffic
