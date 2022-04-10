import encodings
import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,"links")
f1=open("test.txt","r")
l1=f1.readlines()
l2=[]
for i in l1:
    l2.append(i.strip('\n'))
l3=[]
for i in l2:
    l3.append(i.split())

def exel_writer(a,b,filename,c=0,d=0,):
    s=1
    wb = Workbook()
    sheet1 = wb.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,"links")
    for i in range(a,b):
        s1=f"http://127.0.0.1:8000/p{i}"
        sheet1.write(s,0,s1)
        s+=1
    for i in range(c,d):
        s1=f"http://127.0.0.1:8000/p{i}"
        sheet1.write(s,0,s1)
        s+=1
    wb.save(f'{filename}.xls')

print(l3)
for i in range(len(l3)):
    filename=l3[i][0]
    sw=int(l3[i][1])
    a=int(l3[i][2])
    b=int(l3[i][3])
    print(sw)
    if sw==1:
        c1=int(l3[i][4])
        d1=int(l3[i][5])
        exel_writer(a,b,filename,c=c1,d=d1)
    else:
        exel_writer(a,b,filename)
    print(f"completed executing {filename}")