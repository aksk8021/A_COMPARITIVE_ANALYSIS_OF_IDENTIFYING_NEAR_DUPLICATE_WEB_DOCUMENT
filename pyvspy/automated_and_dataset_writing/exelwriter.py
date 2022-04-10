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
for i in range(10):
    # if i==32 or i==33 or i==34 or i==35 or i==36 or i==37 or i==39 or i==93: 
    #     continue
    s1=f"http://127.0.0.1:8000/p1"
    sheet1.write(s,0,s1)
    s+=1
# for i in range(130,172):
#     if i==30 or i==18:
#         continue
#     s1=f"http://127.0.0.1:8000/p{i+1}"
#     sheet1.write(s,0,s1)
#     s+=1  
wb.save(f'custom.xls')