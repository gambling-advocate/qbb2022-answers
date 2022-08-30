# QBB2022 - Day 2 - Lunch Exercises Submission

1. my final full code is uploaded separately in a file called finalcode.py

2. I found that the median was 3. the code i used was

```
#!/usr/bin/env python3

import sys
import statistics
from bed_parser import parse_bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    exons = []
    exons.append(bed[9])
    print(statistics.median(exons))
```