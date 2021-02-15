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
			yu=impb[-1].split('=')
			end_l.append(yu[-1].rstrip('\n'))
new_fl=open('c.txt','a')
new_list=[]
for h in range(l):
	a_usnr=dfs['PartTXT'][h]
	a_usnr=a_usnr.split(":")
	new_list.append(a_usnr[-1].rstrip('\n'))

c=1
for x in new_list:
	if x in end_l:
		new_fl.write(str(c)+' '+'USNR'+x+' '+'USN'+x)
		new_fl.write('\n')
	else:
		new_fl.write(str(c)+' '+'USNR'+x+' '+'NA')
		new_fl.write('\n')
