# MetaProgramming and Debugging

---
Simon Jakobsson (simja649) and
Axel Gard (axega544)



## MetaProgramming

## Profiling in Julia

### Julia's built in Profiling

We ran the `@profile` and noticed that
the print_to_string took a lot of time of the completion and we noticed quickly
that the s variable was inside the for loop but not when we were printing it,
making it take longer to run. So we moved the variable within the if statement and
the code ran much faster.

[full profiling result](profiling/profiling-results.md)

```bash
../julia/julia-1.5.0/bin/julia test.jl
  0.079943 seconds (301.17 k allocations: 30.943 MiB)
List entry 0.9962931752772799
nothing
Overhead ╎ [+additional indent] Count File:Line; Function
=========================================================
  ╎74 @Base/client.jl:506; _start()

.....

13╎    ╎     13 @Base/stream.jl:965; uv_write_async(::Base.TTY, ::Ptr{UInt8}, ::UInt64)
 1╎1  @Base/strings/io.jl:135; print_to_string(::String, ::Vararg{Any,N} where N)
Total snapshots: 80

```


```bash
../julia/julia-1.5.0/bin/julia test.jl
  0.008292 seconds (3.78 k allocations: 713.047 KiB)
List entry 0.9902902159909008
nothing
Overhead ╎ [+additional indent] Count File:Line; Function
=========================================================
 ╎18 @Base/client.jl:506; _start()

.....

3╎    ╎    ╎ 3  @Base/task.jl:704; poptask(::Base.InvasiveLinkedListSynchronized{Task})
Total snapshots: 20

```

### Valgrind

`valgrind --tool=callgrind ../julia/julia-1.5.0/bin/julia test.jl`

original result

```bash
==1833576== Callgrind, a call-graph generating cache profiler
==1833576== Command: ../julia/julia-1.5.0/bin/julia test.jl
==1833576==
....
  2.019582 seconds (301.21 k allocations: 30.943 MiB)
List entry 0.9992942262680331
Trial(1.924 s)
==1833576==
==1833576== Events    : Ir
==1833576== Collected : 9954212169
==1833576==
==1833576== I   refs:      9,954,212,169
```


with fix the result

```bash
==1778827== Callgrind, a call-graph generating cache profiler
==1778827== Command: ../julia/julia-1.5.0/bin/julia test.jl
....
  0.148073 seconds (4.00 k allocations: 731.188 KiB)
List entry 0.9968774338902957
Trial(147.368 ms)
==1778827==
==1778827== Events    : Ir
==1778827== Collected : 9141915434
==1778827==
==1778827== I   refs:      9,141,915,434
```




## General-purpose debugging and profiling

### 1.

When we used GDB we found out that when i = 9 we get a divisible by zero error
(denom = 0). One way to resolve this problem is that we make either an exception
when i=9 that we wont divide denom or ignore when denom = 0.


result from gdb

```gdb
Reading symbols from dividearrays...
(gdb) run
Starting program: /home/axega544/Projects/repositories/tdde45-arch/tdde45-lab5-metaprogramming-and-debugging/debugging/dividearrays

Program received signal SIGFPE, Arithmetic exception.
0x000055555555531c in main (argc=1, argv=0x7fffffffd4b8) at dividearrays.cpp:12
12	    res[i] = nom / denom;
(gdb) p nom
$1 = 9
(gdb) p denom
$2 = 0
(gdb) p i
$3 = 9
```

#### 2.
When we used GDB we found out that the threading had the multiple writers problem which can be seen
in the terminal commandos below. Where the different threads had same current data or
skipped some numbers counting up. To fix this we used a mutex lock (from the pthread in lab instructions) to force completion
of one thread before starting the other. Thus fixing the multiple writers problem.

```
Thread 3 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$6 = 3
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff6d6e700 (LWP 2169112)]

Thread 4 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$7 = 3
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff656d700 (LWP 2169113)]

Thread 5 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$8 = 4
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff7d70700 (LWP 2169110)]

Thread 2 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$9 = 4
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff756f700 (LWP 2169111)]

Thread 3 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$10 = 6
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff6d6e700 (LWP 2169112)]

Thread 4 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$11 = 7
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff656d700 (LWP 2169113)]

Thread 5 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$12 = 7
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff7d70700 (LWP 2169110)]

Thread 2 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$13 = 9
(gdb) continue
Continuing.
[Switching to Thread 0x7ffff756f700 (LWP 2169111)]

Thread 3 "workitems" hit Breakpoint 2, launchThread (in=0x5555555592a0) at workitems.c:24
24	    data->fn(&data->data[n]);
(gdb) p data->current
$14 = 9

```


### fileutil

Both solutions returns the correct hash sum of the bible. 
```
md5sum bible.txt
651592fe7d463428483dc3a927aaadf7  bible.txt

# for not_main
md5sum copy.txt
651592fe7d463428483dc3a927aaadf7  copy.txt

# from main
md5sum copy.txt
651592fe7d463428483dc3a927aaadf7  copy.txt
```    


----
# Reflection report seminar 6

At the seminar we discussed how we understood metaprogramming and how we all used
the debugging tools to find a solution. We found out pretty quickly that all of us
have used the debugging tools pretty much the same and had the same notion of what
you could use metaprogramming for. However, we had a problem with the last task
where we got stack smashing. We got some advice from the other groups to increase
the buffer larger at line to not get overflow, which we changed in the lab and
got a working solution.

We still feel like finding solutions in lower level languages is harder than
higher level languages like julia, where we found a solution quickly. Also, we
find that using debugging tools were pretty easy because we have used gdb and
valgrind before, and found solutions quickly.

We would recommend next year's students to use a hash sum like md5sum to
compare that the copied file is a perfect copy.
