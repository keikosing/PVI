
#change the working directory
import os 
print("Current working directory is '"+ os.getcwd()+"'")
wd=r'C:\allMYfiles\BOX\my_sandbox\from_start'
os.chdir(wd) ##also could use %cd
print("Working directory changed to '"+ os.getcwd()+"'")

#import CSV
import csv
data=[]
print(data)

with open ('001_shortshort2.csv') as out2:
	sreader=csv.reader(out2, delimiter=',',  quotechar='|')
	for row in sreader:
		if row[0] in ['BS', 'BE']:
			data.append(row)
		elif row[0] not in ['BS', 'BE']:
			row[0]=eval(row[0])
			row[1]=eval(row[1])
			data.append(row)
#evaluate------------------------------------------
