# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 March 17 edited 2022 March 21
# Machine Exercise 2

import math

# Input Benchmark Details
name = input("Enter Benchmark Name: ")
elev = float(input("Enter Benchmark Elevation: "))#elev for value
print("")

# Data list 
total_dist = 0 #Distance between first to itself is 0 (benchmark to itself)
sta= [name] #Add initial name to the list
bs = []
fs =[""] #First element remains blank
hi =[]
elevs = [elev] #add initial elevation to the list #elevs for title place
dist_bm = [total_dist] #add initial total_distance
corr = []
adj_elev = []

# Initializing
ask = "Y"
num = 1

# Loop for setups

while ask == "Y" or ask == "y":
    print("Setup:", num)
    bs_val = input(f"Backsight Reading ({name}): ") #check lang kung gagana ba yung f din dito
    name = input("Name of the Next Station (Foresight): ")
    sta.append(name) #New name added to list
    fs_val = input("Foresight Reading ({}): ".format(name))

# Computing BS
    bs_ur = float(bs_val[0:5])
    bs_mr = float(bs_val[6:11])
    bs_lr = float(bs_val[12:]) 
    bs_ave = (bs_ur + bs_mr + bs_lr)/3 #Compute Average of BS
    bs_ave = round(bs_ave,3)
    bs.append(bs_ave)#Add to backsight list

# Computing FS
    fs_ur = float(fs_val[0:5])
    fs_mr = float(fs_val[6:11])
    fs_lr = float(fs_val[12:])
    fs_ave = (fs_ur + fs_mr + fs_lr)/3 #Compute Average of FS
    fs_ave = round(fs_ave,3)
    fs.append(fs_ave)#Add to foresight list

# Computing Height of Instrument
    hi_val = elev + bs_ave
    hi.append(hi_val) #Add to list

# Computing Elevation
    elev = hi_val - fs_ave
    elevs.append(elev) #Add to list

# Computing distance
    #Distance from BS
    bs_dist = (bs_ur - bs_lr) * 100

    #Distance from FS
    fs_dist = (fs_ur - fs_lr) * 100

    #Adding the BS and FS to Total Dist
    total_dist = total_dist + fs_dist + bs_dist
    dist_bm.append(total_dist)

#Number of setup and also last index number
    num +=1 #Remember that num will increase kahit mag N ka
    ask = input("Continue? (Y/N): ")

bs.append("") #adding a blank element to the list to have same no of elements with the other lists 
hi.append("")

# Complete lists atm (STA, BS, HI, FS, Elevs, Dist_BM) need to complete (Corr, Adj_Elev)

# Solving the Correction parts 
# Solving the error of the theo and obs
num = num - 1 # Maximum number of index 
err = elevs[0]-elevs[num]

#Solving the correction for each distance

for dst in dist_bm:
    corr_val = (dst / dist_bm[num]) * err #bakit nung may negative to namali sagot ko? naging positive sya omgee 
    corr.append(corr_val)
    
#Adding the corrections to the distance from the benchmark
    #Initializing the values first
    
num += 1 
for adj in range(num):
   adj_val = elevs[adj]+corr[adj]
   adj_elev.append(adj_val)

# All list are now complete 
corr.pop(0)#Removing the first value of the list since this should be a blank space
corr.insert(0,"")#Inserting a black space as the first item on the list
print("")

# Output for the title bar
print(f"{'Sta' : <5}{'BS' : ^10}{'HI' : ^10}{'FS' : ^10}{'Elevs' : ^10}", end ="") #try lang yung end baka gumana
print(f"{'Dist_BM' : ^10}{'Corr' : ^10}{'Adj_Elev' : >10}")

# Output for the first line (Different output as there is a string on the first row)
print(f"{sta[0] : <5}{bs[0] : ^10.3f}{hi[0]: ^10.3f}{fs[0]: ^10}{elevs[0]: ^10.3f}",end ="")#walang f yung kay FS at Corr kasi string
print(f"{dist_bm[0]: ^10.3f}{corr[0] : ^10}{adj_elev[0]: >10.5f}")

#Print output for values except the last line 
for i in range(1,num-1): #num-1 because range does not include the final row
    print(f"{sta[i] : <5}{bs[i] : ^10.3f}{hi[i]: ^10.3f}{fs[i]: ^10.3f}{elevs[i]: ^10.3f}",end = "")
    print(f"{dist_bm[i]: ^10.3f}{corr[i] : ^10.5f}{adj_elev[i]: >10.5f}")

#Output for final row have strings so it cannot be formatted with the print above due to float values
j = num-1 #num-1 because yung last row yung focus
print(f"{sta[j] : <5}{bs[j] : ^10}{hi[j]: ^10}{fs[j]: ^10.3f}{elevs[j]: ^10.3f}{dist_bm[j]: ^10.3f}{corr[j] : ^10.5f}{adj_elev[j]: >10.5f}")#walang f yung kay BS and HI
