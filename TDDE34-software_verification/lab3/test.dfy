method foo(n: int) returns (r: int)
requires 0 <= n
ensures r == n*n
{
    var i := 0;
    r := 0;
    while (i < n)
    invariant 0 <= i <= n;
    invariant r == i * i;
    decreases n - i;
    {
        r := r + 2*i + 1;
        i := i + 1;
    }
}