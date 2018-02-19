file_text=open("DNA.txt").read()
total=len(file_text)

G=0
C=0
for i in range(len(file_text)):
    if file_text[i]=="G":
        G = G+1.0
    elif file_text[i]=="C":
        C = C+1.0
    sum= G+C
print "DNA:", (file_text)
print "Total characters in DNA:", total
print "Sum of C and G:", sum
print "Total percentage of C+G in DNA Sequence:", (sum/total)*100, "%"
