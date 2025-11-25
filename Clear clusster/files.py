import os

for i in range(15):
    
    with open(f"Data{i}.png","w") as f:
        f.write(f'this is {i}')


files = os.listdir()
for i in range(len(files)):
    for name in files:
        if name.endswith(".png"):
            os.rename(name , f'{i}.png')