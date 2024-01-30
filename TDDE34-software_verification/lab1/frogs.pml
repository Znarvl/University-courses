#ifndef N
	#define N	6
#endif

int a[N+1];	



proctype frog(int place){
	do
	:: true ->
		atomic{
		if 
			:: (a[place] == 1 && place < N && a[place + 1] == 0 ) ->
				a[place] = 0;
				place = place + 1;
				a[place] = 1;
			:: (a[place] == 1 && place < N - 1 && a[place + 2] == 0 ) ->
				a[place] = 0;
				place = place + 2;
				a[place] = 1;
			:: (a[place] == 2 && place > 0 && a[place - 1] == 0 ) ->
				a[place] = 0;
				place = place - 1;
				a[place] = 2;
			:: (a[place] == 2 && place > 1 && a[place - 2] == 0 ) ->
				a[place] = 0;
				place = place - 2;
				a[place] = 2;
			:: else -> break;
		fi
		}
	od

}

proctype monitor(){
assert(
	a[0] != 2 ||
	a[1] != 2 ||
	a[2] != 2 ||
	a[3] != 0 ||
	a[4] != 1 ||
	a[5] != 1 ||
	a[6] != 1
);


}

init{
	int count = 0;
	do
	:: (count < N/2) ->
		a[count] = 1;
		count++;
	:: (count == N/2) ->
		a[count] = 0;
		count++;
	:: (count > N/2 && count < N + 1) ->
		a[count] = 2;
		count++;
	:: count > N -> break;
	od
	
	atomic{
	count = 0;
	do
	:: count < N + 1 && count != N/2 ->
		run frog(count);
		count++;
	:: count == N/2 -> count++;
	:: count > N -> break;
	od
	run monitor();
	}
}
