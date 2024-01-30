datatype Color = Red | White | Blue | Yellow

predicate Below(c1 : Color, c2: Color)
{

    c1 == Red || c1 == c2 || c2 == Yellow || (c1 == White && c2 != Red)
}

method DutchFlag (a: array<Color>)
    modifies a
    ensures forall i,j :: 0 <= i < j < a.Length ==> Below(a[i], a[j])
    ensures multiset(a[..]) == multiset(old(a[..]))
{
    var r, w, b, y := 0, 0, a.Length, a.Length;
    while w < b
        invariant 0 <= r <= w <= b <= y <= a.Length
        invariant forall i :: 0 <= i < r ==> a[i] == Red
        invariant forall i :: r <= i < w ==> a[i] == White
        invariant forall i :: b <= i < y ==> a[i] == Blue
        invariant forall i :: y <= i < a.Length ==> a[i] == Yellow
        decreases b - w
        invariant multiset(a[..]) == multiset(old(a[..]))
        {
            match a[w]
            case Red =>
                a[r], a[w] := a[w], a[r];
                r, w := r+1, w+1;
            case White =>
                w := w+1;
            case Blue =>
                a[b-1], a[w] :=  a[w], a[b-1];
                b := b - 1;
            case Yellow =>
                a[b-1], a[w] :=  a[w], a[b-1];
                a[y-1], a[b-1] := a[b-1], a[y-1];
                y, b := y - 1, b - 1;
        }
}