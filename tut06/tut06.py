import csv
import os
from tkinter import N
os.system("cls")
import numpy as np
import calendar
import datetime

#from datetime import datetime
start_time = datetime.datetime.now()

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

    if os.path.exists("output"):
        for f in os.listdir("output"):
            os.remove(os.path.join("output",f))
        os.rmdir("output")

    curr  = os.getcwd()
    os.mkdir(curr.replace('\\','/')+"/output/")
    os.chdir("output")

    def days(date):
        day = datetime.datetime.strptime(date,'%d-%m-%Y').weekday()
        return (calendar.day_name[day])

    list_date = []
    for i in range(1,m):
        if timestamp[i][0:10] not in list_date and (days(timestamp[i][0:10])=='Monday' or days(timestamp[i][0:10])=='Thursday'):
            list_date.append(timestamp[i][0:10])
    
    total_att = []
    real_att = []
    dupl_att = []
    for i in range(n-1):
        total_att.append([0]*len(list_date))
        real_att.append([0]*len(list_date))
        dupl_att.append([0]*len(list_date))
    
    for i in range(1,m):
        if timestamp[i][0:10] in list_date:
            a = list_date.index(timestamp[i][0:10])
            b = rollNo.index(attendance[i][0:8])
            total_att[b-1][a]+=1
            if timestamp[i][11:13]=='14' or timestamp[i][11:] =='15:00':
                real_att[b-1][a]=1
                dupl_att[b-1][a]+=1
    


    for i in range(1,n):
        from openpyxl import Workbook
        book = Workbook()
        sheet = book.active
        rows = [["Date","Roll","Name","Total Attendance Count","Real","Duplicate","Invalid","Absent"]]
        rows.append(["",rollNo[i],name[i]])
        for j in range(len(list_date)):
            rows.append([list_date[j],"","",total_att[i-1][j],real_att[i-1][j],dupl_att[i-1][j]-real_att[i-1][j],total_att[i-1][j]-dupl_att[i-1][j],1-real_att[i-1][j]])
        for row in rows:
            sheet.append(row)
        book.save(rollNo[i] + '.xlsx')

    from openpyxl import Workbook
    book = Workbook()
    sheet = book.active
    rows1 = []
    rows1.append(["Roll","Name"])
    for r in list_date:
        rows1[0].append(r)
    rows1[0].append("Actual Lecture Taken")
    rows1[0].append("Total Real")
    rows1[0].append("% Attendance")
    for i in range(1,n):
        rows1.append([rollNo[i],name[i]])
        for j in range(len(list_date)):
            if real_att[i-1][j]==1:
                rows1[i].append("P")
            else:
                rows1[i].append("A")
        rows1[i].append(np.sum(len(list_date)))       
        rows1[i].append(np.sum(real_att[i-1]))
        rows1[i].append(np.round_((np.sum(real_att[i-1])/np.sum(len(list_date)))*100,2))
    for row in rows1:
        sheet.append(row)
    book.save('attendance_report_consolidated.xlsx')
            


attendance_report()
print("*****************************************************     run successfully     ******************************************************")
end_time = datetime.datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))