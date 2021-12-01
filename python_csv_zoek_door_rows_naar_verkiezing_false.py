import pandas as pd
print("go")

dtf = pd.read_csv("uitslagen.csv",sep=";")
#print(dtf.columns)
#allecodes = dtf[['RegioCode','GeldigeStemmen']][5:12]
allecodes = dtf

#print(allecodes[3:4])
#print(allecodes)

for i,x in allecodes.iterrows():
	if int(x['RegioCode'][-1]) % 2 == 0 :
#		print(type(x.isnull()))
#		print(x.isnull().index)
		r = 0
		for y in x.isnull():
			if not y and r > 9:
				print(x.index[r])
		#	else:
		#		print(">>>>>>false>>>"+x.index[r])
			r += 1
		print("=================")


