#!/usr/bin/env python3

import sys
#importing sys module

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    #what type of data object the info from the header should be
    format_description = {}
    #formatting of the genotype info
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    #matching the data type in the header to a useable python function
    malformed = 0
    #initializing malformed variable
    
    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
#trying to open an input file, if the file is not there an error is raised

    for h, line in enumerate(fs):
        if line.startswith("#"):
#for loop. h and line are both variables, enumerate returns the index number and line
#if statement will deal will header until it ends.
            try:
        #the entire try block is ensuring things are properly formatted
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else:
            try:
    #this whole block is keeping track of the variants formatting 
                fields = line.rstrip().split("\t")
        #this line is stripping the ending of the lines and splitting by tabs
                fields[1] = int(fields[1])
        #checking for the 2nd position and converting it to an integer
                if fields[5] != ".":
                    fields[5] = float(fields[5])
        #if the quality (6th) value is not just a "." we want to convert to a float
                info = {}
            #creating the info dictionary
                for entry in fields[7].split(";"):
            #for the variable "entry" in the 8th position of the line in fields, we are taking anything split by a ; and making it into separate list entries
                    temp = entry.split("=")
                #temp is becoming a list that takes all the info in entry and creates separate list entries with anything split by an "=".
                    if len(temp) == 1:
            #this is specifically looking at anything that was not split by an equal sign and setting the key temp[0] in the info dictionary = to a None value
                        info[temp[0]] = None
                    else:
            #if there is an = sign and 2 values we will set name and value as the key 
                        name, value = temp
            #info_type dictionary is being pulled from the header section and being assigned to the variable Type
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
                #Using the name, which was set as the key in the dictionary, to find what type of info it is (float, int, str) 
                fields[7] = info
        #taking the 8th entry in fields and setting that equal to info
                if len(fields) > 8:
        #if there's more than 8 fields, which are the genotype information and format. If there is less than 8 fields then there isn't any genotype info.
                    fields[8] = fields[8].split(":")
            #we are taking the 9th column, making a list split by colons, and storing it back in the 9th column
                    if len(fields[8]) > 1:
            #If we have greater than 1 format field in the 9th column
                        for i in range(9, len(fields)):
                #for each index in the range from 10th column to the end, indicated by len(fields)
                            fields[i] = fields[i].split(':')
                #turning the genotype field for i and turning it into a list split by colons
                    else:
                        fields[8] = fields[8][0]
            #we are taking the 9th thing in the list fields, and then taking the 0th thing in that list.
                vcf.append(fields)
        #After we made alllll those changes to fields, we are finally adding it appending it the vcf list.
            except:
                malformed += 1
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
#if there were any malformed entries print the above statement. Prints it to stderr instead of stdout.
    return vcf
    #return makes sure there is actually an output

if __name__ == "__main__":
    fname = sys.argv[1]
    #whatever you put in after your script
    vcf = parse_vcf(fname)
    #running the function on the this file name, stored into a variable vcf
    for i in range(10):
        print(vcf[i])