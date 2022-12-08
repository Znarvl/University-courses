clear;
close all;
load datatraffic;

%Make bar plot of traffic with function of time
bar(years, traffic)
xlabel('Year');
ylabel('Data')
title('Data traffic')
legend('Video', 'File transfer', 'Web and other')
