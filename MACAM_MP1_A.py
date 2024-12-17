# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 April 16
# Machine Problem
# MP1_A

import math
import MACAM_MP1_B
from MACAM_MP1_B import *

# Data list
r_lname = {} 
r_ldist = {}
r_lbrng = {}
coordinates = {}


# Initializing values for the sentinel-controlled loop
data_no = 1
ask = "Y" 

while ask == "Y" or ask == "y":
    if data_no == 1:
        line_name = input(f"Enter name of Line {data_no}: ")
        r_lname[data_no] = line_name  #Adding the name to the data list
        line_dist = float(input(f"Enter distance of Line {line_name}: "))
        r_ldist[data_no] = line_dist
        line_brng = input(f"Enter bearing of Line {line_name}: ")
        r_lbrng[data_no] = line_brng
        crds = input(f"Enter Point {line_name[0]} Coordinates (E,N):  ")
        coordinates[data_no] = tuple(float(x) for x in crds.split(","))
        ask = input("Enter new line? ")
        data_no += 1
    else:
        line_name = input(f"Enter name of Line {data_no}: ")
        r_lname[data_no] = line_name  #Adding the name to the data list
        line_dist = float(input(f"Enter distance of Line {line_name}: "))
        r_ldist[data_no] = line_dist
        line_brng = input(f"Enter bearing of Line {line_name}: ")
        r_lbrng[data_no] = line_brng
        ask = input("Enter new line? ")
        data_no += 1
        

#Computation of values
azi = convertAzimuth(r_lbrng)
latdep = computeLD(r_ldist,azi)
lecrec = computeLECREC(latdep,r_ldist)
acc = deterAcc(lecrec)

#Correction Rule input
print()
method = "initial"
while not(method == "COMPASS" or method == "compass" or method == "TRANSIT" or method == "transit"):
        method = input("Enter traverse adjustment method (compass/transit): ")

if method == "compass" or method == "COMPASS":
    corr = computeCorrCompass(r_ldist,latdep)
else: #automatically transit na to
    corr = computeCorrTransit(latdep)

#Computation of adjusted values
adjLD = computeAdjLND(latdep,corr) #latitude and departure
adjDB = computeAdjDistBear(adjLD) #distance and bearing 
adjC = computeAdjCoordinates(coordinates,adjLD)#coordinates

#computation of area
area_dict = areaDMD(adjLD) #dictionary where in the last key contains area

#for printing purposes mag cocombine tayo kasi yon need sa isang part
given = {}
for i in range(1,data_no):
    given[i] = [r_lname[i], r_ldist[i], r_lbrng[i], latdep[i]] #{1: [name,dist,bearing,[lat,dep]]

print()
printLECREC(lecrec,acc)
print()
printAdj(given,corr,adjLD)
print()
printAdjDNB(r_lname,adjDB)
print()
printAdjCoordinates(r_lname,adjC)
print()
printAreaComp(r_lname,adjLD,area_dict)

        






