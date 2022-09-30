Great work! You just about nailed the implementation, there are just a few minor issues:

When you're initializing the traceback matrix, I think you want the first row to have `1` and the first column to have `2` (which is the opposite of what you have now). The first row should be representing gaps in seq1, which you're filling in as `1` later in your code (-0.25)

For traceback, your while condition is `i>0 and j>0`, but that will actually terminate as soon as either i or j become 0, which is not what we want if there are leading gaps. Because of this, your count for the number of gaps in the DNA alignment is slightly off (-0.25)

One last thing: we don't want you having two giant blocks of code that are doing the same thing but for the DNA or AA. Rather, anything that's going to change between AA and DNA should be read in as an input. So you should have one input each for 1) the input fasta, 2) the scoring matrix file, 3) the gap penalty, 4) the output file. (-1)

8.5/10
