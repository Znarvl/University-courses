using BenchmarkTools
using Random
using Profile

function f()
  lst = rand(50000)
  for i in lst
      s = "List entry $(i)\r" # The \r makes it so the terminal isn't filled
    if i > 0.99
        print(s)
    end
  end
end

f()
@time f()
x = @benchmark f()
#x = @profile f()
println()
println(x)

#Profile.print()
