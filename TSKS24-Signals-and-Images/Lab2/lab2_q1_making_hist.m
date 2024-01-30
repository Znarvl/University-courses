%Showing signals in a histogram
%H1 = histogram(x1, 100);    %plotting the histogram for x1 with 100 bins
%H2 = histogram(x2, 100);    %plotting the histogram for x2 with 100 bins
hold on                     %for two histograms in same figure
histogram(x1, 100);
histogram(x2, 100);
%Writing out so we can see information about the histograms in H1 and H2
%H1
%H2
hold off