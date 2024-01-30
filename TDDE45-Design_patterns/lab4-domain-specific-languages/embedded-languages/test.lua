-- Adds x to the result of the fromC function, which is defined in the C-file
function addFromC ( x, y )
  return x + fromC(y)
end
