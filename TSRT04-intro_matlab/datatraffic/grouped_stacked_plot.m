clear;
close all;
load datatraffic;

%we need a subplot with 2x1 matrix, hence 2,1 then last is plotnumber
%Create a subplot for the picture above with grouped bar
subplot(2,1,1);
bar(years, traffic, 'grouped'); %string grouped defines usage of grouped function
xlabel('Year');
ylabel('Data');
title('Data traffic grouped');
legend('Video', 'File transfer', 'Web and other');

%Create a subplot for the picture above with stacked bar
subplot(2,1,2)
bar(years, traffic, 'stacked'); %string grouped defines usage of stacked function
xlabel('Year');
ylabel('Data');
title('Data traffic stacked');
legend('Video', 'File transfer', 'Web and other');

