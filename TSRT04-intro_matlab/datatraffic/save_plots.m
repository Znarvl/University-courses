%Get each script and save them to respectivly format
%gcf returns the current figure, and if a figure doesnt exist gcf creates a
%figure 
hold on;
line_plot
saveas(gcf, 'line_plot.fig')
saveas(gcf, 'line_plot.png')
saveas(gcf, 'line_plot.jpg')
saveas(gcf, 'line_plot.pdf')
saveas(gcf, 'line_plot.eps')

hold on;
line_plot_total
saveas(gcf, 'line_plot_total.fig')
saveas(gcf, 'line_plot_total.png')
saveas(gcf, 'line_plot_total.jpg')
saveas(gcf, 'line_plot_total.pdf')
saveas(gcf, 'line_plot_total.eps')

hold on;
line_plot_print
saveas(gcf, 'line_plot_print.fig')
saveas(gcf, 'line_plot_print.png')
saveas(gcf, 'line_plot_print.jpg')
saveas(gcf, 'line_plot_print.pdf')
saveas(gcf, 'line_plot_print.eps')

hold on;
grouped_stacked_plot
saveas(gcf, 'grouped_stacked.fig')
saveas(gcf, 'grouped_stacked.png')
saveas(gcf, 'grouped_stacked.jpg')
saveas(gcf, 'grouped_stacked.pdf')
saveas(gcf, 'grouped_stacked.eps')

hold on;
bar_plot
saveas(gcf, 'grouped_stacked.fig')
saveas(gcf, 'grouped_stacked.png')
saveas(gcf, 'grouped_stacked.jpg')
saveas(gcf, 'grouped_stacked.pdf')
saveas(gcf, 'grouped_stacked.eps')




