%2.6 Monte-carlo-simulation
function result = monte_carlo(dice, amount)
    result = zeros(1,amount); %create vector with the amount of experiments

    for i = 1:amount
        result(i) = five_of_a_kind(dice); % use function from 2.5 to iterate over amount of simulation wanted to be done
    end
    
    histogram(result, 'BinWidth', 1); %set staples to width 1
    xlabel('Number of throws')
    ylabel('Frequency')

end