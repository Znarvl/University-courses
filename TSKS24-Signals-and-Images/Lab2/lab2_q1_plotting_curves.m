%Plotting of afforementioned signals

hold on                     %Use if plotting togeather
%plot(t,x1);                 %plot x1
plot(t,x2);                 %plot x2
axis([0 0.625e-3 -1 1]);    %fitting the plot window for 5 periods of x1
%stem(t,x1);                 %plotting samples for x1
stem(t,x2);                 %plotting samples for x2
hold off                    %if hold was used