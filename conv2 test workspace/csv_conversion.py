r="C:\Users\mjasper\Documents\_GIS\Code Snippets\SnipsDwld\conv2 test workspace"

indat = open("dups.txt","r").readlines()
n = len(indat)
outdat = "("
for i in range(n):
    outst = (indat[i])
    outstring = outst+","
    outdat += outstring
outdat.rstrip(",")
outfile = open("dups_output2.txt","w")
print >> outfile, outdat
