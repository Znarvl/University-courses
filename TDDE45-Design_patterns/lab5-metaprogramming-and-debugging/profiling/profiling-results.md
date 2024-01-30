## Profiling in Julia

### Julia's built in Profiling

#### original result  

```
../julia/julia-1.5.0/bin/julia test.jl
  0.079943 seconds (301.17 k allocations: 30.943 MiB)
List entry 0.9962931752772799
nothing
Overhead ╎ [+additional indent] Count File:Line; Function
=========================================================
  ╎74 @Base/client.jl:506; _start()
  ╎ 74 @Base/client.jl:296; exec_options(::Base.JLOptions)
  ╎  74 @Base/Base.jl:368; include(::Module, ::String)
 3╎   74 @Base/Base.jl:380; include(::Function, ::Module, ::String)
  ╎    1  @Base/compiler/typeinfer.jl:601; typeinf_ext(::Core.MethodInstance, ::UInt64)
  ╎     1  @Base/compiler/typeinfer.jl:570; typeinf_ext(::Core.MethodInstance, ::Core.Compiler.Params)
  ╎    ╎ 1  @Base/compiler/typeinfer.jl:21; typeinf(::Core.Compiler.InferenceState)
  ╎    ╎  1  @Base/compiler/typeinfer.jl:149; finish
 1╎    ╎   1  @Base/compiler/typeinfer.jl:291; type_annotate!(::Core.Compiler.InferenceState)
 1╎    1  ...ab5-metaprogramming-and-debugging/profiling/test.jl:0; f()
  ╎    55 ...ab5-metaprogramming-and-debugging/profiling/test.jl:8; f()
  ╎     55 @Base/strings/io.jl:174; string
 1╎    ╎ 1  @Base/strings/io.jl:124; print_to_string(::String, ::Vararg{Any,N} where N)
  ╎    ╎ 9  @Base/strings/io.jl:133; print_to_string(::String, ::Vararg{Any,N} where N)
  ╎    ╎  9  @Base/iobuffer.jl:112; Type##kw
  ╎    ╎   8  @Base/iobuffer.jl:114; Base.GenericIOBuffer{Array{UInt8,1}}(; read::Bool, write::Bool, append::Noth...
  ╎    ╎    6  @Base/iobuffer.jl:31; StringVector
 3╎    ╎     3  @Base/strings/string.jl:60; _string_n
 3╎    ╎     3  @Base/strings/string.jl:71; unsafe_wrap
  ╎    ╎    2  @Base/iobuffer.jl:91; Type##kw
  ╎    ╎     2  @Base/iobuffer.jl:98; #IOBuffer#330
  ╎    ╎    ╎ 2  @Base/iobuffer.jl:27; GenericIOBuffer
 2╎    ╎    ╎  2  @Base/iobuffer.jl:20; GenericIOBuffer
  ╎    ╎   1  @Base/iobuffer.jl:121; Base.GenericIOBuffer{Array{UInt8,1}}(; read::Bool, write::Bool, append::Noth...
 1╎    ╎    1  @Base/array.jl:428; fill!
 3╎    ╎ 45 @Base/strings/io.jl:135; print_to_string(::String, ::Vararg{Any,N} where N)
 1╎    ╎  1  @Base/strings/io.jl:34; print(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64)
  ╎    ╎  39 @Base/strings/io.jl:35; print(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64)
  ╎    ╎   39 @Base/ryu/Ryu.jl:112; show
  ╎    ╎    28 @Base/ryu/Ryu.jl:113; show(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64, ::Bool, ::Bool)
  ╎    ╎     28 @Base/iobuffer.jl:31; StringVector
 4╎    ╎    ╎ 4  @Base/strings/string.jl:60; _string_n
23╎    ╎    ╎ 24 @Base/strings/string.jl:71; unsafe_wrap
  ╎    ╎    6  @Base/ryu/Ryu.jl:115; show(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64, ::Bool, ::Bool)
  ╎    ╎     5  @Base/ryu/shortest.jl:306; writeshortest
  ╎    ╎    ╎ 1  @Base/ryu/shortest.jl:17; reduce_shortest
 1╎    ╎    ╎  1  @Base/int.jl:463; <<
  ╎    ╎    ╎ 3  @Base/ryu/shortest.jl:73; reduce_shortest
  ╎    ╎    ╎  1  @Base/ryu/utils.jl:138; mulshiftsplit
  ╎    ╎    ╎   1  @Base/ryu/utils.jl:55; mulshift
  ╎    ╎    ╎    1  @Base/int.jl:461; >>
 1╎    ╎    ╎     1  @Base/int.jl:455; >>
  ╎    ╎    ╎  2  @Base/ryu/utils.jl:140; mulshiftsplit
  ╎    ╎    ╎   2  @Base/ryu/utils.jl:55; mulshift
  ╎    ╎    ╎    1  @Base/int.jl:461; >>
 1╎    ╎    ╎     1  @Base/int.jl:455; >>
 1╎    ╎    ╎    1  @Base/int.jl:471; rem
  ╎    ╎    ╎ 1  @Base/ryu/shortest.jl:147; reduce_shortest
 1╎    ╎    ╎  1  @Base/int.jl:86; +
 1╎    ╎     1  @Base/ryu/shortest.jl:340; writeshortest
  ╎    ╎    5  @Base/ryu/Ryu.jl:117; show(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64, ::Bool, ::Bool)
  ╎    ╎     1  @Base/array.jl:1090; resize!
 1╎    ╎    ╎ 1  @Base/array.jl:901; _deleteend!
  ╎    ╎     4  @Base/io.jl:645; write
  ╎    ╎    ╎ 1  @Base/abstractarray.jl:1006; pointer
 1╎    ╎    ╎  1  @Base/pointer.jl:65; unsafe_convert
  ╎    ╎    ╎ 3  @Base/io.jl:622; unsafe_write
  ╎    ╎    ╎  2  @Base/iobuffer.jl:426; unsafe_write(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Ptr{UInt8}, ::UInt64)
 2╎    ╎    ╎   2  @Base/int.jl:86; +
  ╎    ╎    ╎  1  @Base/iobuffer.jl:430; unsafe_write(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Ptr{UInt8}, ::UInt64)
  ╎    ╎    ╎   1  @Base/promotion.jl:409; max
 1╎    ╎    ╎    1  @Base/int.jl:82; <
 1╎    ╎  2  @Base/strings/io.jl:185; print(::Base.GenericIOBuffer{Array{UInt8,1}}, ::String)
  ╎    ╎   1  @Base/strings/io.jl:183; write
  ╎    ╎    1  @Base/iobuffer.jl:426; unsafe_write(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Ptr{UInt8}, ::UInt64)
 1╎    ╎     1  @Base/int.jl:86; +
  ╎    14 ...ab5-metaprogramming-and-debugging/profiling/test.jl:10; f()
 1╎     14 @Base/coreio.jl:3; print(::String)
  ╎    ╎ 13 @Base/strings/io.jl:185; print(::Base.TTY, ::String)
  ╎    ╎  13 @Base/strings/io.jl:183; write
  ╎    ╎   13 @Base/stream.jl:1005; unsafe_write(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
  ╎    ╎    13 @Base/stream.jl:922; uv_write(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
13╎    ╎     13 @Base/stream.jl:965; uv_write_async(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
 1╎1  @Base/strings/io.jl:135; print_to_string(::String, ::Vararg{Any,N} where N)
Total snapshots: 80

```

#### Improved results

```
../julia/julia-1.5.0/bin/julia test.jl
  0.008292 seconds (3.78 k allocations: 713.047 KiB)
List entry 0.9902902159909008
nothing
Overhead ╎ [+additional indent] Count File:Line; Function
=========================================================
 ╎18 @Base/client.jl:506; _start()
 ╎ 18 @Base/client.jl:296; exec_options(::Base.JLOptions)
 ╎  18 @Base/Base.jl:368; include(::Module, ::String)
7╎   18 @Base/Base.jl:380; include(::Function, ::Module, ::String)
 ╎    1  @Base/compiler/typeinfer.jl:601; typeinf_ext(::Core.MethodInstance, ::UInt64)
 ╎     1  @Base/compiler/typeinfer.jl:568; typeinf_ext(::Core.MethodInstance, ::Core.Compiler.Params)
 ╎    ╎ 1  @Base/compiler/inferencestate.jl:118; Core.Compiler.InferenceState(::Core.Compiler.InferenceResult, ::Bool, ::Core.C...
1╎    ╎  1  @Base/compiler/utilities.jl:110; retrieve_code_info
 ╎    2  ...lab5-metaprogramming-and-debugging/profiling/test.jl:9; f()
1╎     2  @Base/strings/io.jl:174; string
 ╎    ╎ 1  @Base/strings/io.jl:135; print_to_string(::String, ::Vararg{Any,N} where N)
 ╎    ╎  1  @Base/strings/io.jl:35; print(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64)
 ╎    ╎   1  @Base/ryu/Ryu.jl:112; show
 ╎    ╎    1  @Base/ryu/Ryu.jl:113; show(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Float64, ::Bool, ::Bool)
 ╎    ╎     1  @Base/iobuffer.jl:31; StringVector
1╎    ╎    ╎ 1  @Base/strings/string.jl:60; _string_n
 ╎    8  ...lab5-metaprogramming-and-debugging/profiling/test.jl:10; f()
1╎     8  @Base/coreio.jl:3; print(::String)
 ╎    ╎ 7  @Base/strings/io.jl:185; print(::Base.TTY, ::String)
 ╎    ╎  7  @Base/strings/io.jl:183; write
 ╎    ╎   7  @Base/stream.jl:1005; unsafe_write(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
 ╎    ╎    4  @Base/stream.jl:922; uv_write(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
3╎    ╎     4  @Base/stream.jl:965; uv_write_async(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
 ╎    ╎    3  @Base/stream.jl:933; uv_write(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
 ╎    ╎     3  @Base/task.jl:712; wait
3╎    ╎    ╎ 3  @Base/task.jl:704; poptask(::Base.InvasiveLinkedListSynchronized{Task})
Total snapshots: 20

```


### Valgrind

#### original
```
==1833576== Callgrind, a call-graph generating cache profiler
==1833576== Copyright (C) 2002-2017, and GNU GPL'd, by Josef Weidendorfer et al.
==1833576== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==1833576== Command: ../julia/julia-1.5.0/bin/julia test.jl
==1833576==
==1833576== For interactive control, run 'callgrind_control -h'.
==1833576== brk segment overflow in thread #1: can't grow to 0x4847000
==1833576== (see section Limitations in user manual)
==1833576== NOTE: further instances of this message will not be shown
--1833576-- WARNING: unhandled amd64-linux syscall: 1008
--1833576-- You may be able to write your own handler.
--1833576-- Read the file README_MISSING_SYSCALL_OR_IOCTL.
--1833576-- Nevertheless we consider this a bug.  Please report
--1833576-- it at http://valgrind.org/support/bug_reports.html.
  2.019582 seconds (301.21 k allocations: 30.943 MiB)
List entry 0.9992942262680331
Trial(1.924 s)
==1833576==
==1833576== Events    : Ir
==1833576== Collected : 9954212169
==1833576==
==1833576== I   refs:      9,954,212,169

```

#### with fix
```
==1778827== Callgrind, a call-graph generating cache profiler
==1778827== Copyright (C) 2002-2017, and GNU GPL'd, by Josef Weidendorfer et al.
==1778827== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==1778827== Command: ../julia/julia-1.5.0/bin/julia test.jl
==1778827==
==1778827== For interactive control, run 'callgrind_control -h'.
==1778827== brk segment overflow in thread #1: can't grow to 0x4847000
==1778827== (see section Limitations in user manual)
==1778827== NOTE: further instances of this message will not be shown
--1778827-- WARNING: unhandled amd64-linux syscall: 1008
--1778827-- You may be able to write your own handler.
--1778827-- Read the file README_MISSING_SYSCALL_OR_IOCTL.
--1778827-- Nevertheless we consider this a bug.  Please report
--1778827-- it at http://valgrind.org/support/bug_reports.html.
  0.148073 seconds (4.00 k allocations: 731.188 KiB)
List entry 0.9968774338902957
Trial(147.368 ms)
==1778827==
==1778827== Events    : Ir
==1778827== Collected : 9141915434
==1778827==
==1778827== I   refs:      9,141,915,434
```
