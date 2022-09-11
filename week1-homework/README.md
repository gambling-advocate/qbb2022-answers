1.1 1,000,000bp * 5x coverage = 5Mbp
	5Mbp / 100bp/read = 50,000 reads 
	150,000 reads for 15x coverage

1.2 did it, code uploaded in question1.py

1.3 7018 is the toatl number, I used np.count_nonzero to total up the amount zero values in my array, here is that code:
```
x = np.array(genome)
zero = x == 0
meh = np.count_nonzero(zero)
```

1.4 did it, code uploaded in question1_4.py and histograms.