from datetime import datetime
start_time = datetime.now()
import numpy as np
import os
os.system("cls")
def scorecard():
	name_of_player = [[],[]]
	fileObject = open("teams.txt","r")
	data = fileObject.readlines()
	for i in range(len(data)-1):
		a=0
		for j in range(len(data[i])):
			if data[i][j] == " " and a==0:
				name_of_player[i//2].append(data[i][0:j])
				a=1
			if data[i][j] == ":":
				a = j+2
			if data[i][j] ==",":
				name_of_player[i//2].append(data[i][a:j])
				a = j+2
		name_of_player[i//2].append(data[i][a:len(data[i])-1])
		i+=1

	file1 = open("Scorecard.txt","w")
	for k in range(2):
		if k==0:
			p = "Pakistan Innings"
			filename = "pak_inns1.txt"
		else:
			p = "India Innings"
			filename = "india_inns2.txt"
		total =0
		out=''
		wiket=0
		ball =0
		extra = ['b',0,'lb',0,'w',0,'nb',0,'p',0]
		fileObject = open(filename, "r")
		data = fileObject.readlines()
		list_sc = [["Batter"],[""],["R"],["B"],["4s"],["6s"],["SR"]]
		list_bo = [["Bowler"],["O"],["M"],["R"],["W"],["NB"],["WD"],["ECO"]]
		for i in range(len(data)):
			y=0
			a=0
			x=0
			if data[i][0:3]=='6.1':
				powerplay = total
			for j in range(len(data[i])):
				if data[i][j] ==" " and a==0:
					a = j+1
				if data[i][j:j+2] == 'to' and x==0:
					x = j+3
				if data[i][j] == ',':
					y = j
					name = data[i][x:y]
					name1 = data[i][a:x-4]
					if name1 not in list_bo[0]:
						list_bo[0].append(name1)
						for ankur in range(1,8):
							list_bo[ankur].append(0)
					if name not in list_sc[0]:
						list_sc[0].append(name)
						list_sc[1].append("not out")
						for ankur in range(2,6):
							list_sc[ankur].append(0)
					run = data[i][y+2:]
					b = list_sc[0].index(name)
					c = list_bo[0].index(name1)
					if run[0:4] == 'wide':
						list_bo[3][c]+=1
						list_bo[6][c]+=1
						total+=1
						extra[5]+=1
					if 'wides' in run:
						if run[2:6] == 'runs':
							list_bo[3][c]+=int(run[0])
							list_bo[6][c]+=int(run[0])
							total+=int(run[0])
							extra[5]+=int(run[0])
						if run[0:4] == 'FOUR':
							list_bo[3][c]+=4
							list_bo[6][c]+=4
							total+=4
							extra[5]+=4
					if run[0:6] == 'no run' or run[0:4] =='byes' or run[0:8]=='leg byes':
						list_sc[3][b]+=1
						list_bo[1][c]+=1
						ball+=1
						if run[0:4] =='byes':
							if run[8:11] == 'run':
								total+=int(run[6])
								extra[1]+=int(run[6])
							if run[6:10] == 'FOUR':
								total+=4
								extra[1]+=4
						if run[0:8]=='leg byes':
							if run[12:15] == 'run':
								total+=int(run[10])
								extra[3]+=int(run[10])
							if run[10:14] == 'FOUR':
								total+=4
								extra[3]+=4
					if run[2:5] == 'run':
						list_sc[2][b]+=int(run[0])
						list_sc[3][b]+=1
						list_bo[1][c]+=1
						list_bo[3][c]+=int(run[0])
						total+=int(run[0])
						ball+=1
					if run[0:4] == 'FOUR':
						list_sc[2][b]+=4
						list_sc[3][b]+=1
						list_sc[4][b]+=1
						list_bo[1][c]+=1
						list_bo[3][c]+=4
						total+=4
						ball+=1
					if run[0:3] == 'SIX':
						list_sc[2][b]+=6
						list_sc[3][b]+=1
						list_sc[5][b]+=1
						list_bo[1][c]+=1
						list_bo[3][c]+=6
						total+=6
						ball+=1
					if run[4:7]=='Lbw':
						list_sc[1][b] ='lbw b ' + data[i][a:x-4]
						list_sc[3][b]+=1
						list_bo[1][c]+=1
						list_bo[4][c]+=1
						wiket+=1
						ball+=1
						out = out + str(total)+'-'+str(wiket)+'('+list_sc[0][b]+','+str(ball//6)+'.'+str(ball%6)+'), '
					if run[4:10]=='Caught':
						d = data[i].index("!!")
						list_sc[1][b] = 'c '+ data[i][y+16:d] + ' b ' + data[i][a:x-4]
						list_sc[3][b]+=1
						list_bo[1][c]+=1
						list_bo[4][c]+=1
						wiket+=1
						ball+=1
						out = out + str(total)+'-'+str(wiket)+'('+list_sc[0][b]+','+str(ball//6)+'.'+str(ball%6)+'), '
					if run[4:10]=='Bowled':
						list_sc[1][b]='b ' + data[i][a:x-4]
						list_sc[3][b]+=1
						list_bo[1][c]+=1
						list_bo[4][c]+=1
						wiket+=1
						ball+=1
						out = out + str(total)+'-'+str(wiket)+'('+list_sc[0][b]+','+str(ball//6)+'.'+str(ball%6)+'), '
					break
			i+=1
		for i in range(1,len(list_sc[1])):
			list_sc[6].append(np.round_((list_sc[2][i]/list_sc[3][i])*100,2))

		for i in range(len(list_sc[0])):
			for j in range(len(name_of_player[k])):
				if list_sc[0][i] in name_of_player[k][j]:
					list_sc[0][i] = name_of_player[k][j]
				if list_bo[0][i%len(list_bo[0])] in name_of_player[1-k][j]:
					list_bo[0][i%len(list_bo[0])] in name_of_player[1-k][j]

		did_not_play = []
		for i in range(1,len(name_of_player[k])-1):
			for j in range(len(list_sc[0])):
				if list_sc[0][j] in name_of_player[k][i]:
					break
				if j==len(list_sc[0])-1:
					did_not_play.append(name_of_player[k][i])

		file1 = open("Scorecard.txt","a")
		file1.write(f"{p : <90}{str(total)+'-'+str(wiket)+'('+str(ball//6)+'.'+str(ball%6)+' Ov)' : <50}"'\n')
		for i in range(0,len(list_sc[0])):
			file1.write(f"{list_sc[0][i] : <25}{list_sc[1][i] : <40}{list_sc[2][i] : <10}{list_sc[3][i] : <10}{list_sc[4][i] : <10}{list_sc[5][i] : <10}{list_sc[6][i] : <10}"'\n')
		file1.write(f"{'Extras':<90}{str(extra[1]+extra[3]+extra[5]+extra[7]+extra[9])+'('+'b '+str(extra[1])+', lb '+str(extra[3])+', w '+str(extra[5])+', nb'+str(extra[7])+', p '+str(extra[9])+')':<50}"'\n')
		file1.write(f"{'Total' : <90}{str(total)+'('+str(wiket)+'wkts, '+str(ball//6)+'.'+str(ball%6)+' Ov)' : <50}"'\n\n')
		if len(did_not_play)!=0:
			file1.write(f"{'Did not Bat':<40}")
			file1.write(did_not_play[0])
			for j in range(1,len(did_not_play)-1):
				file1.write(","+did_not_play[j])
		file1.write("\n\nFall of Wickets\n")
		file1.write(out+'\n\n')
		file1.write(f"{list_bo[0][0] : <25}{list_bo[1][0] : <30}{list_bo[2][0] : <10}{list_bo[3][0] : <10}{list_bo[4][0] : <10}{list_bo[5][0] : <10}{list_bo[6][0] : <10}{list_bo[7][0] : <10}"'\n')
		for i in range(1,len(list_bo[0])):
			file1.write(f"{list_bo[0][i] : <25}{str(int(list_bo[1][i])//6)+'.' + str(int(list_bo[1][i])%6) : <30}{list_bo[2][i] : <10}{list_bo[3][i] : <10}{list_bo[4][i] : <10}{list_bo[5][i] : <10}{list_bo[6][i] : <10}{str(np.round_((int(list_bo[3][i])/int(list_bo[1][i]))*6,1)) : <10}"'\n')
		file1.write(f"\n\n{'Powerplays':<45}{'Powerplays':<45}{'Runs':<45}"'\n')
		file1.write(f"{'Mandatory':<45}{'0.1-6':<45}{str(powerplay):<45}"'\n\n')

scorecard()
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
