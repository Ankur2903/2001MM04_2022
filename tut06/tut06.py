import csv
import os
from tkinter import N
os.system("cls")

from datetime import datetime
start_time = datetime.now()
import numpy as np

def attendance_report():
    rollNo = []
    name = []
    n =0
    with open("input_registered_students.csv","r") as file:
        reader = csv.reader(file)
        for x in reader:
            rollNo.append(x[0])
            name.append(x[1])
            n = n+1
    
    m =0
    timestamp = []
    attendance = []
    with open("input_attendance.csv","r") as file:
        reader = csv.reader(file)
        for x in reader:
            timestamp.append(x[0])
            attendance.append(x[1])
            m = m+1

    list_class =["28/07","01/08","04/08","08/08","11/08","15/08","18/08","22/08","25/08","29/08","01/09","05/09","08/09","12/09"]
    dict_rollno ={}
    dict_attendance_count_actual = {}
    dict_attendance_count_fake = {}
    for i in range(1,n):
        dict_rollno[rollNo[i]]=0
        dict_attendance_count_actual[rollNo[i]]=0
        dict_attendance_count_fake[rollNo[i]]=0
    Total_count_of_attendance_on_that_day = ["Total_count_of_attendance_on_that_day"]
    timestamp_1 = ["Timestamp"]
    rollNo_1 = ["Rollno"]
    name_1 = ["name"]

    dict_rollno[attendance[1][0:8]]+=1
    if timestamp[1][0:5] in list_class and timestamp[1][11:13]=="14":
        dict_attendance_count_actual[attendance[1][0:8]]+=1
    else:
        dict_attendance_count_fake[attendance[1][0:8]]+=1
    x = 1
    for i in range(2,m):
        if attendance[i]=='' or attendance[i][0:8] not in dict_rollno.keys():
            continue
        if timestamp[i][0:10]==timestamp[x][0:10]:
            dict_rollno[attendance[i][0:8]]+=1
            if timestamp[i][0:5] in list_class and timestamp[i][11:13]=="14":
                dict_attendance_count_actual[attendance[i][0:8]]+=1
            else:
                dict_attendance_count_fake[attendance[i][0:8]]+=1
        else:
            for j in range(1,n):
                if dict_rollno[rollNo[j]]>1:
                    Total_count_of_attendance_on_that_day.append(dict_rollno[rollNo[j]])
                    timestamp_1.append(timestamp[x][0:10])
                    rollNo_1.append(rollNo[j])
                    name_1.append(name[j])
            for k in range(1,n):
                dict_rollno[rollNo[k]]=0
            if timestamp[i][0:5] in list_class and timestamp[i][11:13]=="14":
                dict_attendance_count_actual[attendance[i][0:8]]+=1
            else:
                dict_attendance_count_fake[attendance[i][0:8]]+=1
            dict_rollno[attendance[i][0:8]]+=1
            x = i

    if os.path.exists("output"):
        for f in os.listdir("output"):
            os.remove(os.path.join("output",f))
        os.rmdir("output")

    curr  = os.getcwd()
    os.mkdir(curr.replace('\\','/')+"/output/")
    os.chdir("output")

    with open("attendanc_report_consolidated.csv","w",newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll","Name","total_lecture_taken","attendance_count_actual","attendance_count_fake","attendance_count_absent","Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal "])
    with open("attendanc_report_duplicate.csv","w",newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp","Roll","Name","Total count of attendance on that day"])
    for i in range(1,n):
        with open(rollNo[i]+".csv","w",newline ="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll","Name","total_lecture_taken","attendance_count_actual","attendance_count_fake","attendance_count_absent","Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal "])
            writer.writerow([rollNo[i],name[i],"14",dict_attendance_count_actual[rollNo[i]],dict_attendance_count_fake[rollNo[i]]])
        with open("attendanc_report_consolidated.csv","a",newline ="") as file:
            writer = csv.writer(file)
            writer.writerow([rollNo[i],name[i],"14",dict_attendance_count_actual[rollNo[i]],dict_attendance_count_fake[rollNo[i]]])
        if i<len(name_1):
            with open("attendanc_report_duplicate.csv","a",newline ="") as file:
                writer = csv.writer(file)
                writer.writerow([timestamp_1[i],rollNo_1[i],name_1[i],Total_count_of_attendance_on_that_day[i]])
   
attendance_report()
print("*****************************************************     run successfully     ******************************************************")
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
