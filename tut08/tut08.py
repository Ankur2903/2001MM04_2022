from datetime import datetime
start_time = datetime.now()
import numpy as np
import os
os.system("cls")

def scorecard():
	for k in range(2):
		if k==0:
			print("hi1")
			filename = "pak_inns1.txt"
		else:
			print("Hi2")
			filename = "india_inns2.txt"
		fileObject = open(filename, "r")
		data = fileObject.readlines()
		list_sc = [["Batter"],[""],["R"],["B"],["4s"],["6s"],["SR"]]
		for i in range(len(data)):
			y=0
			a=0
			c=0
			x=0
			for j in range(len(data[i])):
				if data[i][j] ==" " and a==0:
					a = j+1
				if data[i][j] =="!" and c==0:
					c = j
				if data[i][j:j+2] == 'to' and x==0:
					x = j+3
				if data[i][j] == ',':
					z = y
					y = j
					if z==0:
						name = data[i][x:y]
						if name not in list_sc[0]:
							list_sc[0].append(name)
							list_sc[1].append("not out")
							list_sc[2].append(0)
							list_sc[3].append(0)
							list_sc[4].append(0)
							list_sc[5].append(0)
					if z!=0:
						run = data[i][z+2:y]
						b = list_sc[0].index(name)
						if run == 'no run' or run =='byes':
							list_sc[3][b]+=1
						if run == '1 run':
							list_sc[2][b]+=1
							list_sc[3][b]+=1
						if run == '2 runs':
							list_sc[2][b]+=2
							list_sc[3][b]+=1
						if run == '3 runs':
							list_sc[2][b]+=3
							list_sc[3][b]+=1
						if run == 'FOUR':
							list_sc[2][b]+=4
							list_sc[3][b]+=1
							list_sc[4][b]+=1
						if run == 'SIX':
							list_sc[2][b]+=6
							list_sc[3][b]+=1
							list_sc[5][b]+=1
						if run[4:7]=='Lbw':
							list_sc[1][b] ='lbw b ' + data[i][a:x-4]
							list_sc[3][b]+=1
						if run[4:10]=='Caught':
							list_sc[1][b] = 'c '+ data[i][z+16:c] + ' b ' + data[i][a:x-4]
							list_sc[3][b]+=1
						if run[4:10]=='Bowled':
							list_sc[1][b]='b ' + data[i][a:x-4]
							list_sc[3][b]+=1
						break
			i+=1
		for i in range(1,len(list_sc[1])):
			list_sc[6].append(np.round_((list_sc[2][i]/list_sc[3][i])*100,2))
		
		print(list_sc)

	
	file1 = open("Scorecard.txt","w")
	for i in range(len(list_sc[0])):
		file1.write(f"{list_sc[0][i] : <25}{list_sc[1][i] : <40}{list_sc[2][i] : <10}{list_sc[3][i] : <10}{list_sc[4][i] : <10}{list_sc[5][i] : <10}{list_sc[6][i] : <10}")
		file1.write("\n")
	

scorecard()
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
