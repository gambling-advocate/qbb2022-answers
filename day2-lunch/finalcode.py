#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        #not allowing bed10 or bed11 files to run
        if fieldN < 3 or fieldN in range(9,12) or fieldN >12:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue    
        #matching the field_types/conversions to the fields, allowing "." to pass           
        for j in range(min(len(field_types), len(fields))):
            if fields[j] != ".":
                fields[j] = field_types[j](fields[j])
        #splitting the itemRGB into a list of 3 distinct values    
        if len(fields[8].split(",")) == 3:
            fields[8] = fields[8].split(",")
            for h in range(3):
                fields[8][h] = int(fields[8][h])
            
        bed.append(fields)
            
    fs.close()
    return bed
#printing results
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    print(bed)
