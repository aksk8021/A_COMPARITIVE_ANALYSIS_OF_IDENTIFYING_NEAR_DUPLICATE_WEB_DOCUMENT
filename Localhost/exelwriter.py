import encodings
import xlwt
from xlwt import Workbook
wb = Workbook()
a=1
b=1
s=1
al=112
sheet1 = wb.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,"links")
for i in range(803):
    s1=f"http://127.0.0.1:8000/p{i+1}"
    sheet1.write(s,0,s1)
    s+=1
for i in range(803):
    s1=f"http://127.0.0.1:8000/p{i+1}"
    sheet1.write(s,0,s1)
    s+=1  
wb.save(f'u800_800.xls')