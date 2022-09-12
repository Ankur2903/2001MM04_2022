import numpy as np
def octact_identification(mod=5000):
    time = []
    u = []
    v = []
    w = []
    u_ = []
    v_ = []
    w_ = []
    octant = []
    total = [0]*8

    import csv
    import os
    os.system("cls")
    with open("octant_input.csv","r") as file:
        reader = csv.reader(file)
        i=0
        for x in reader:
            if i==0:
                time.append(x[0])
                i = i+1
            else:
                time.append(x[0])
                u.append(float(x[1]))
                v.append(float(x[2]))
                w.append(float(x[3]))
                
        n = len(u)
        avg_of_u = np.mean(u)
        avg_of_v = np.mean(v)
        avg_of_w = np.mean(w)

        for i in range(n):
            v_.append(v[i]-avg_of_v)
            u_.append(u[i]-avg_of_u)
            w_.append(w[i]-avg_of_w)

        for i in range(n):
            if u_[i]>=0 and v_[i]>=0 and w_[i]>0:
                octant.append(1)
            elif u_[i]<0 and v_[i]>=0 and w_[i]>0:
                octant.append(2)
            elif u_[i]<0 and v_[i]<0 and w_[i]>=0:
                octant.append(3)
            elif u_[i]>=0 and v_[i]<0 and w_[i]>=0:
                octant.append(4)
            elif u_[i]>=0 and v_[i]>=0 and w_[i]<=0:
                octant.append(-1)
            elif u_[i]<0 and v_[i]>=0 and w_[i]<=0:
                octant.append(-2)
            elif u_[i]<0 and v_[i]<0 and w_[i]<0:
                octant.append(-3)
            else:
                octant.append(-4)
        
        for j in range(0,n):
            if octant[j] ==1:
                total[0] = total[0] +1
            elif octant[j] ==2:
                total[2] = total[2] +1
            elif octant[j] ==3:
                total[4] = total[4] +1
            elif octant[j] ==4:
                total[6] = total[6] +1
            elif octant[j] ==-1:
                total[1] = total[1] +1
            elif octant[j] ==-2:
                total[3] = total[3] +1
            elif octant[j] ==-3:
                total[5] = total[5] +1
            else:
                total[7] = total[7] +1

    with open("octant_output.csv","w",newline = "") as file:
        writer = csv.writer(file)
        for i in range(n+1):
            if i==0:
                writer.writerow(["Time","U","V","W","U Avg","V Avg","W Avg","U'=U - U avg","V'=V - V avg","W'=W - w avg","Octant","","Octant ID","1","-1","2","-2","3","-3","4","-4"])
            elif i==1:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),str(avg_of_u),str(avg_of_v),str(avg_of_w),u_[i-1],v_[i-1],w_[i-1],str(octant[i-1]),"","Overall Count",str(total[0]),str(total[1]),str(total[2]),str(total[3]),str(total[4]),str(total[5]),str(total[6]),str(total[7])])
            elif i==2:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1],str(octant[i-1]),"User Input","Mod "+ str(mod)])
            elif i==3:
                 writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1],str(octant[i-1]),"",str((i-3)*mod)+"-"+str((i-2)*mod)])
            elif i>3 and i<=3+(n-1)/mod:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1],str(octant[i-1]),"",str((i-3)*mod+1)+"-"+str((i-2)*mod)])
            else:
                 writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1],str(octant[i-1]),"",""])

mod=5000
octact_identification(mod)