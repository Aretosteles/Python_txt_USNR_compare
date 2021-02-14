import pandas as pd

dfs = pd.read_csv('File1_importA.csv')
l=len(pd.read_csv('File1_importA.csv'))
a=open('ImportB.txt','r')
b=a.readlines()
end_l=[]
for g in b:
	impb=g.split(' ')
	if 'USNR'in impb[-1]:
		if impb not in end_l: 
			end_l.append(impb[-1])
new_fl=open('c.txt','a')
new_list=[]
for h in range(l):
	a_usnr=dfs['PartTXT'][h]
	a_usnr=a_usnr.split(":")
	new_list.append(a_usnr[-1])

c=0
for el in new_list:
	c+=1
	if el in new_list:
		new_fl.write(str(c)+' '+el+'\n') 

