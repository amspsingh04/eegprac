# %%
import os
import shutil

# %%
source_root='E:\eeg-motor-movementimagery-dataset-1.0.0\\'
destination_root='E:\EEG_MMIDB'

# %%


# %%
source=[]
for i in range (1,110):
    for j in range(1,10):
        if(i<10):
            source.append(source_root+f"files\S00{i}\S00{i}R0{j}.edf")
        elif(i<100 and i>=10):
            source.append(source_root+f"files\S0{i}\S0{i}R0{j}.edf")
        elif(i>100):
            source.append(source_root+f"files\S{i}\S{i}R0{j}.edf")
    for j in range(10,16):
        if(i<10):
            source.append(source_root+f"files\S00{i}\S00{i}R{j}.edf")
        elif(i<100 and i>=10):
            source.append(source_root+f"files\S0{i}\S0{i}R{j}.edf")
        elif(i>100):
            source.append(source_root+f"files\S{i}\S{i}R{j}.edf")
for i in range(1,1620):
    print(source[i])

# %%


# %%
