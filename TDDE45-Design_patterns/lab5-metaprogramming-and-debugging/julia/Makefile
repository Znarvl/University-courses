.PHONY: run

VERSION=1.5.0

run: julia-$(VERSION)/bin/julia
	$< run.jl

shell: julia-$(VERSION)/bin/julia
	$<

julia-%/bin/julia: julia-%-linux-x86_64.tar.gz
	tar xzf $<
	$@ -e 'using Pkg; Pkg.add("BenchmarkTools"); Pkg.add("StatProfilerHTML")'
	touch $@
julia-%-linux-x86_64.tar.gz:
	wget https://julialang-s3.julialang.org/bin/linux/x64/`echo $@ | grep -E -o [0-9]+[.][0-9]+`/$@
