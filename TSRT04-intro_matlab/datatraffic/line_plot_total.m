clear;
close all;
load datatraffic;
hold on;

%sum all vectors of each row
plot(years, sum(traffic,2)) % sum along the dimensions, which is 2
plot(years, traffic(:,1))
plot(years, traffic(:,2))
plot(years, traffic(:,3))

xlabel('Year');
ylabel('Data')
title('Total data traffic')
legend('Total traffic','Video', 'File transfer', 'Web and other')