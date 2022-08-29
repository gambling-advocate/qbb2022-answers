# QBB2022 - Day 1 - Homework Exercises Submission

1. for nuc in A C G T
do
```
  echo "Considering " $nuc
  awk -v ver=$nuc '/^#/{next} {if ($4 ==ver) {print $5}}' $1 | sort | uniq -c
```
done

1. The error was with the if statment including a bash variable, which needed to be converted to an awk variable. The results make sense.