%Part 2.1 several throws
%creates vector with the probability of the amount of dices that are thrown

function vector = throw(n)
    vector = zeros(1,n); % create a vector with 0s with element from 1 to the amount of dices thrown
    for i = 1:n
        vector(i) = ceil(rand()*6); %iterate over each element, give them a random value between 0 to 1 and multiply
    end
end