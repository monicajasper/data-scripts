#Conversion 1 Script
#Author: Monica Jasper
#Date: 2016

#conv1.py does the 1st conversion step for data in a specific format -
#IDs delineated by row are reformatted into quoted, comma-separated text
#for easy use into SQL and other code


#set environment workspace as r
r = ""

#read input file; see conv1 test workspace folder for test input file 
indat = open("01_input.txt","r").readlines()
n = len(indat)
outdat = "("

#iterate through each line, add quotes and comma after, strip return
for i in range(n):
    outnum = int(indat[i])
    outstring = "'%8.8i"%outnum+"', "
    outdat += outstring
outdat.rstrip(",")

#set output file name to open
outfile = open("01_output.txt","w")

#write to output file
print >> outfile, outdat
