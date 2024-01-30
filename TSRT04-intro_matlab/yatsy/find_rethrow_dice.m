%2.4
function result = find_rethrow_dice(n)
    size = length(n); %amount 
    result = []; %create empty array
    for i = 1:size
        %if not most common, put it in array
        if (n(i) ~= most_throws(n)) % ~= is not equal in matlab
            result =  [result i]; % if the value is not equal to the most common, place it in the result array
        end
    end
end