
enum {Locked, Unlocked} lock = Locked;

int foo();

int KeAcquireSpinLock(){
    if(lock == Locked)
        ERROR:;
    else
        lock = Locked;
    return(1);
}

int KeReleaseSpinLock(){
    if(lock == Unlocked)
        ERROR:;
    else
        lock = Unlocked;
    return(1);
}

typedef struct Lock Lock;

int main(){

    int nPacketsOld = 0; 
    int nPackets    = 0;

    do
    {
        
        KeAcquireSpinLock();

        nPacketsOld = nPackets;

        if(nPackets < foo())
        {
            KeReleaseSpinLock();
            nPackets++;

        }
    }while(nPackets != nPacketsOld);

    KeReleaseSpinLock();

    return(0);
}


