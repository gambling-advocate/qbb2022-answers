1. I first sorted the aau1043_dnm.csv file using:

`sort -t ',' -k 5,6 aau1043_dnm.csv | cut -d, -f5,6 | uniq -c | grep 'mother\|father' > DNMperproband.txt`

1. I then separated the file into two files into maternal and paternal DNMs.

```
 grep 'mother' DNMperproband.csv | cut -d, -f1,2 > motherDNM.csv
 grep 'father' DNMperproband.csv | cut -d, -f1,2 > fatherDNM.csv
```

1. I then rejoined these files into a new file and the sorted that file numerically.
```
join -1 2 -2 2 -t, fatherDNM.csv motherDNM.csv > DNMperproband.csv
sort -g DNMperproband.csv > sortedDNMperproband.csv 
```

1. I then joined that file with the parental age file and created the final sorted file.

`join -t ',' sorted_DNMperproband.csv aau1043_parental_age.csv > finalsort.csv`


3. There is a significant relationship between maternal age and maternally inherited de novo mutations. The p-value is 6.878e-24. The size of this relationship is that for every 1 year increase in age, we expect about 0.3776 increase in De novo mutations.

4. There is a significant relationship between maternal age and maternally inherited de novo mutations. The p-value is 1.552e-84. The size of this relationship is that for every 1 year increase in age, we expect about 1.3538 increase in De novo mutations.

6. The number of mutations inherited from mother and father was significantly different. Probands seem to inherit far more DNMs from their fathers. The p-value was 6.665e-15

7. The predicted number of DNMs for proband born to a 50.5 year old father is 78.7. The reason for this is that our intercept value is 10.3263 and our coefficient between # of DNMs and age is 1.3538. Using y = mx+ b I arrived at this number.