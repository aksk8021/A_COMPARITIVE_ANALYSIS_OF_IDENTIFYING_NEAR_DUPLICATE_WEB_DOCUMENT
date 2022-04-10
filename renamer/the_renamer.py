import os
# os.rename('a.html','lol.html')
j=0
for i in range(503,803):
    os.rename(f'p{i-502}.html',f'p{i}.html')