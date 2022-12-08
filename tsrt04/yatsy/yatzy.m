function [mhat, s2hat]= yatzy(simulations)
    x = monte_carlo_expected_variance(5, simulations);
    e1 = [1; 0;0;0;0];
    e5 = [0;0;0;0;1];
    A = [0 1/6 1/36 1/258 1/1296;
        0 5/6 10/36 15/216 25/1296;
        0 0 25/36 80/216 250/1296;
        0 0 0 120/216 900/ 1296;
        0 0 0 0 120/1296];
    probabilities = zeros(1, max(x));
    for k = 1:max(x)
        probabilities(k) = e1' * A^k * e5 * simulations;
    end
    hold on
    plot(probabilities)
end