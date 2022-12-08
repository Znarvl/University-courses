%2.7
function [x, expected, variance] = monte_carlo_expected_variance(dice, simulations)
    x = monte_carlo(dice, simulations); %get result from monte carlo simulation

    expected = mean(x); %Find expected value by taking the mean

    variance = 0; % create variance var and set it to 0 initially
    for i = 1:simulations
        variance = variance + (x(i) - expected)^2; %Def of variance from equation
    end
    
    variance = variance/(simulations - 1); % Add the last bit of variance, 1/n-1
    hold on
    plot(expected)
end