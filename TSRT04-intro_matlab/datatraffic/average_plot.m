clear;
close all;
load datatraffic;
%9,7 million swedish citizens
tot_swe_citizen = 9.7 * 10^6;

%Convert from petabyte to gigabyte (10^6) and apply per
%citizen(tot_swe_citizen)
gigabyte_traffic = traffic * 10^6 / tot_swe_citizen;


plot(years, gigabyte_traffic);
xlabel('Year');
ylabel('Data gigabyte');
title('Data traffic');
legend('Video', 'File transfer', 'Web and other');


%2018 amount of video should be 6.3gig, which is fairly low