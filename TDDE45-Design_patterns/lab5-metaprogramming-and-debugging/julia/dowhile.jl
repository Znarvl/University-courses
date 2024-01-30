macro doWhile(block, cond)
  println("__source__ ", __source__)
  println("cond ", cond)
  println("block ", block)
  res = quote
    #error("TODO: Your code here")
    block
    while cond
        block
    end
  end
  println(res) # For debugging; should not print any lines referencing dowhile.jl if doing the optional part
  res
  println("\n\n\n")

end
