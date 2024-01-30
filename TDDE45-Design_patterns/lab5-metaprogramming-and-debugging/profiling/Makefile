.PHONY: run

VERSION=1.5.0

run: ../julia/julia-$(VERSION)/bin/julia
	$< test.jl

shell: ../julia/julia-$(VERSION)/bin/julia
	$<

../julia/julia-$(VERSION)/bin/julia:
	$(MAKE) -C ../julia julia-$(VERSION)/bin/julia
