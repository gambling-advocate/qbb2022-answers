#Step 1:

I used the provided code to parse my KRAKEN files and called it like this:
```
python krona.py metagenomics_data/step0_givendata/KRAKEN/SRR492* SRR492*
```
I could've written a bash for loop to do all 8 files at once, but because it was only 8 files I just copy and pasted.

I then used ktImportText:
```
ktImportText -q SRR492*_krona.txt -o "SRR492*graph.html"
```
I noticed that by far the most amount of bacteria were from enterococcus faecalis. This makes sense given that is an infant's gut sample.

