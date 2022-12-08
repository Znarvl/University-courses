%2.5
function result = five_of_a_kind(dice)
    throws = find_rethrow_dice(dice); %simulate how many dices are thrown
    result = 1; %Display how many times you need to throw
    while range(throws) ~= 0 % Range checks difference between biggest and smallest number, if it is 0 we got yatsy
        result = result + 1; % If still in loop we add another throw
        throws = find_rethrow_dice(throws); %rethrow dices that are not matched with the most common
    end
end