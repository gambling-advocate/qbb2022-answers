import sys
from vcfParser import parse_vcf
#importing sys and the parse_vcf from vcfParser 

rs = parse_vcf("random_snippet.vcf")
db = parse_vcf("dbSNP_snippet.vcf")
#storing the output from both of the files that I am running throug parse_vcf
    
db_IDs = {}
rs_positions = {}

for line in db:
    if line[0] == "CHROM":
        continue
    #ignore first line of dbSNP
    chrom = line[0]
    pos = line[1]
    ref = line[3]
    IDs = line[2]
    #setting variables for each of the needed info bits to be placed in our dictionary
    db_IDs[(chrom, pos, ref)] = IDs
#grabbing all the info from dbSNP and storing it in a dictionary
counter = 0
for i,things in enumerate(rs):
    #ignore first line again
    if things[0] == "CHROM":
        continue
    chrom = things[0]
    pos = things[1]
    ref = things[3]
#finding all chroms,pos,and ref values in db that are equal to those in SNP
    if (chrom, pos, ref) in db_IDs.keys():
#if there is a match we will replace the value in the 2nd index.
        things[2] = db_IDs[(chrom, pos, ref)]
    else:
        counter = counter + 1
print(counter)
        