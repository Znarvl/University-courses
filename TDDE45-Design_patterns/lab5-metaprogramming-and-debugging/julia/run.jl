"""Template programming is a sort of metaprogramming where you fill
in the blanks, but most parts of the code are very similar."""


# Problem1
for (name,op) in [(:add, :+), (:sub, :-), (:mul, :*)]
    # eval(Meta.parse("$name(x,y) = x $op y"))
    syntax_tree = Expr(:(=), Expr(:call, name, :x, :y), Expr(:block,:(#= none:1 =#), Expr(:call, op, :x, :y)))
    eval(syntax_tree)

  # Create a function that is named for example add and returns the
  # sum of its two arguments
end



@assert 3 == add(1, 2)
@assert -1.0 == sub(1.0, 2.0)
@assert "abc" == mul("ab", "c")


# Problem 2
# TODO: Make an until block for Julia, similar to do {} while (cond); in C
#
# [OPTIONAL] If you want to implement the extra requirement (Make sure that any assertions and error-messages refer to lines in the original code):
#   Hint: You can access a hidden input __source__ in a macro and use that to replace source information.
#   By having the macro in a separate file, you can check source locations that match dowhile.jl and replace them with __source__.

include("dowhile.jl") # Modify the macro in dowhile.jl
function testDoWhile()
  local a = 5
  @doWhile begin
    @assert a < 18
    a += 1
    println(a)
  end a==100
end
testDoWhile()
