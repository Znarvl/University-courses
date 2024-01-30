#ifndef N
	#define N	7
#endif


mtype = {frogr, frogl, no};

mtype a[N];	


proctype P(){
	int count = 0;
	do
	:: do 
		:: (count < N) ->
			if
			:: (a[count] == frogr) ->
				if
				:: count < N - 1 && a[count + 1] == no ->
					a[count] = no;
					a[count + 1] = frogr;
				:: count < N - 2 && a[count + 2] == no ->
					a[count] = no;
					a[count + 2] = frogr;
				fi
				
			:: (a[count] == frogl) ->
				if
				:: count > 0 && a[count - 1] == no ->
					a[count] = no;
					a[count + 1] = frogr;
				:: count > 1 && a[count - 2] == no ->
					a[count] = no;	
					a[count + 2] = frogr;
				fi
			:: else;
			fi
		:: (count == N) -> break;
		od
	od
}


proctype monitor(){
assert(
	a[0] != frogr ||
	a[1] != frogr ||
	a[2] != frogr ||
	a[3] != no ||
	a[4] != frogl ||
	a[5] != frogl ||
	a[6] != frogl
);


}

init{
	a[0] = frogl;
	a[1] = frogl;
	a[2] = frogl;
	a[3] = no;
	a[4] = frogr;
	a[5] = frogr;
	a[6] = frogr;
	atomic{run P();run monitor();}
}
