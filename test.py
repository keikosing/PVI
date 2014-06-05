
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
#make deep copy	
addC=[]
for row in data:
	addC.append(row[:])

#########
#add extra columns
########
for row in addC:
	row[0:0]=['','','']

############################################
#move BS/BE and delete
############################################
#make deep copy	for movement
moveBS=[]
for row in addC:
	moveBS.append(row[:])

def rearrange(M):
	initial_length=len(M)
	N=[]
	rows_deleted=0
	breathnumber=0
	breath_count=0
	print ('Original: '+str(len(M))+'-->Copied: '+str(len(N)))
	while M!=[]:
		if M[0][3]=='BS':
			breathnumber=breathnumber+1
			M[1][0]=str(breathnumber)
			M[1][1]='BS'	
			#del(M[0])
			rows_deleted=rows_deleted+1; breath_count=breath_count+1
		elif M[0][3]=='BE':
			N[-1][1]='BE'
			#del(M[0])
			rows_deleted=rows_deleted+1; breath_count=breath_count+1
		else:
			N.append(M[0])
		del(M[0])
		#print ('Original: '+str(len(M))+'-->Copy: '+str(len(N)))
	else:
		print ('Original: '+str(len(M))+'-->Copied: '+str(len(N))+'\n')
		print (str(initial_length)+" lines processed from original")
		print("Rows Deleted: "+str(rows_deleted)+'\n')
		try:
			print("Breath Count: "+str(breath_count/2))		
			print("Breath Count half of deleted rows? "+str(rows_deleted%(breath_count/2)==0))
		except:
			print("***Already processed***")
			pass
		return N

moveBS=rearrange(moveBS)
