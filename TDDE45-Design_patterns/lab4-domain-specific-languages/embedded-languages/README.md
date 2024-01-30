# Domain-specific languages Embedded languages

---

Simon Jakobsson (simja649)
Axel Gard (axega544)


## Regular expression

### grep
```
[0-9]{7},([1]?[9]|2[2]?[0-3]),.*memory.*
```
```bash
grep -E "[0-9]{7},([1]?[9]|2[2]?[0-3]),.*memory.*" file1.txt

```
66 memory in bible between 19-23

### SED

```
sed 's/"Diana";4;U;/"Diana";2;U;/' file2.txt
sed 's/"Carl";4;U;/"Carl";2;U;/' file2.txt
```


## Reflection report
We learnt about the application of bindings between languages. We learnt how to work the sed
and grep and how grep has different flags (specially the extended -E flag). Under the seminar
we discussed within the group of B and found out that everyone had quite similar solutions.
The biggest dissimilarity was the lua part where people had tried but had different outputs.
We discussed our solution which works and people like the idea with wrappers alot.
We got stuck on the lua part for quite some time because not all had fully solved the lab,
but we think in the end people got the idea and found that the documentation was the key to solve the lab.

What became clear through the lab and the seminar is that our RegEx skills were very ruste,
even when we both have taken and passed TDDD14 Formal Languages and Automata Theory.
Of course we were able to dust off the old skills but this was still clear that the skills were not sharp.

Our strengths this time was that we grasped the lab pretty fast and was kinda comfortable with the
languages before making the task less hard to grasp. We also were keen to read the documentation
better and thus got a good result from the lua lab.

For those taking the course next year I would recommend using more of the official Lua docs for understanding
how to bind Lua and C. It is easy to just use stack overflow or other forms, but the official docs are
usually pretty good. But also for the regular expression part use an online tool like [regexr.com](https://regexr.com/)
to see what is selected.
