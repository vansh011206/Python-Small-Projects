import os

files = os.listdir('Folder')
i = 0
for name in files:
    if name.endswith('.png'):
       os.rename(f'Folder/{name}',f'Folder/{i}.png') 
       i=i+1