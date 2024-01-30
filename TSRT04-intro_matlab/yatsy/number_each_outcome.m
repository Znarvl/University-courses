%2.2
% Summerize how many dices there are of every kind
% By using matlabs built in function categorical and histcounts
% Categorical defines a set of numbers we strive to find
% then the histcounts counts the number of histograms there are,
% Putting them in each category.
function result = number_each_outcome(n)
    C = categorical(n, [1,2,3,4,5,6]);
    result = histcounts(C);
end