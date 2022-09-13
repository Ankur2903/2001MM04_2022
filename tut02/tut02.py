import numpy as np
def octact_identification(mod=5000):
    from openpyxl import load_workbook
    wb = load_workbook("input_octant_transition_identify.xlsx")
    sheet = wb["Sheet1"]
    row_count = sheet.max_row
    #column_count = sheet.max_column

    time =[]
    u = []
    v = []
    w = []

    for i in range(2, row_count + 1):
        time.append(sheet.cell(row=i, column=1).value)#append time value in time list
        u.append(sheet.cell(row=i, column=2).value)
        v.append(sheet.cell(row=i, column=3).value)
        w.append(sheet.cell(row=i, column=4).value)

    avg_of_u = np.mean(u)
    avg_of_v = np.mean(v)
    avg_of_w = np.mean(w)#store avg of u,v,w in avg_of_u,avg_of_v,avg_of_w
        
    from openpyxl import Workbook
    book = Workbook()
    sheet = book.active

    rows = [
        ["Time","U","V","W","U Avg","V Avg","W Avg","U'=U - U avg","V'=V - V avg","W'=W - w avg","Ocatant","","Octant ID","1","-1","2","-2","3","-3","4","-4"]
    ]

    for i in range(row_count-1):
        if i==0:
            rows.append([time[i],u[i],v[i],w[i],avg_of_u,avg_of_v,avg_of_w,u[i]-avg_of_u,v[i]-avg_of_v,w[i]-avg_of_w])
        else:
            rows.append([time[i],u[i],v[i],w[i]," "," "," ",u[i]-avg_of_u,v[i]-avg_of_v,w[i]-avg_of_w])
    
    for row in rows:
        sheet.append(row)
    book.save('output_octant_transition_identify.xlsx')
mod=5000
octact_identification(mod)