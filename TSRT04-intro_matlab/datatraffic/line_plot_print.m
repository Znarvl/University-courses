clear;
close all;
load datatraffic;

hold on;
%plot video with red solid color
plot(years, traffic(:,1), '-r');
%plot filetransfer with dashed black
plot(years, traffic(:,2), '--black');
%plot web and other with dash dot green
plot(years, traffic(:,3), '-.g');

xlabel('Year');
ylabel('Data')
title('Data traffic')
legend('Video', 'File transfer', 'Web and other')
