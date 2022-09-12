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
        

    with open("octant_output.csv","w",newline = "") as file:
        writer = csv.writer(file)
        for i in range(n+1):
            if i==0:
                writer.writerow(["Time","U","V","W","U Avg","V Avg","W Avg","U'=U - U avg","V'=V - V avg","W'=W - w avg","Ocatant","","Octant ID","1","-1","2","-2","3","-3","4","-4"])
            elif i==1:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),str(avg_of_u),str(avg_of_v),str(avg_of_w),u_[i-1],v_[i-1],w_[i-1]])
            elif i==2:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1]])
            elif i==3:
                 writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1]])
            elif i>3 and i<=3+(n-1)/mod:
                writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1]])
            else:
                 writer.writerow([time[i],str(u[i-1]),str(v[i-1]),str(w[i-1]),"","","",u_[i-1],v_[i-1],w_[i-1]])

mod=5000
octact_identification(mod)