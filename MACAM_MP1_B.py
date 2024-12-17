# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 April 16
# Machine Problem
# MP1_B

import math
#Defining the different functions needed

def convertAzimuth(dictionary): #Need lang is bearings data na nasa dictionary
    '''
    This function will convert bearing data to its corresponding azimuth values. 
    This accepts for a bearings in a dictionary data type (Example: {1: "N 45-6-45 E"})
    Returns a dictionary with a key of integers and values of its corresponding
    azimuth values.
    '''
    final = {}
    x = len(dictionary)+1
    for i in range(1, x):
        a = dictionary[i].split() #Spliting using the space
        b = a[1].split("-") #Spliting the dms using -
        deg = float(int(b[0]) + int(b[1])/60 + int(b[2])/3600)

        if a[0]=="S" or a[0]=="s":
            if a[2]=="W" or a[2]=="w":
                final[i] = deg #for SW
            else:
                final[i] = 360 - deg #for SE
        else:
            if a[2]=="E" or a[2]=="e":
                final[i] = 180 + deg #for NE
            else:
                final[i] = 180 - deg #for NW
    return final

def computeLD(dist,azi): #Bearings and distance
    '''
    This function is used to compute the Latitude and Departure of the said lines.
    This will accept a dictionary for both argument where in the first dictionary
    is the distance of the line and the second dictionary is the azimuth of the line.
    This will return a dictionary with values in a list. (Example. {no: [LAT,DEP]})
    '''
    final={}
    lat={}
    dep={}
    x = len(azi)+1
    for i in range(1,x):
        if azi[i]=="90":#DUE WEST
            lat[i]=0
            dep[i]=-dist[i]

        elif azi[i]=="180": #DUE NORTH
            lat[i]=dist[i]
            dep[i]=0

        elif azi[i]=="270": #DUE EAST
            lat[i]=0
            dep[i]=dist[i]

        elif azi[i]=="0" or azi[i]=="360":
            lat[i]=-dist[i]
            dep[i]

        else:
            lat[i]= float((-dist[i])) * math.cos(azi[i]*(math.pi/180))
            dep[i]= float((-dist[i])) * math.sin(azi[i]*(math.pi/180))
            
        final[i]=[lat[i],dep[i]] #Adding a list into a dictionary [LAT, DEP] form
    return final #{no: [LAT,DEP]}

def computeLECREC(latdep,dist): #lat dept at distance
    '''
    This function is used to compute the LEC and REC of the traverse. This will accept
    a two dictionaries that containts the latitude and departure and the distance of the
    line. This will return a tuple containing the LEC and REC. Example (LEC, REC).
    '''
    lat = 0
    dep = 0
    dst = 0
    x = len(latdep)+1
    for i in range(1,x):
        lat += latdep[i][0]
        dep += latdep[i][1]
        dst += dist[i]
    lec = math.sqrt(lat**2 + dep**2)
    rec = int(round(dst/lec,-3))
    final = (lec, f"1/{rec}")
    return final #tuple yung ending (lec,rec)

def deterAcc(lecrec):#YUNG VALUES BHIE DI Q SURE TO FLEECE
    '''
    This functions determine the highest horizontal control accuracy standard of the
    traverse. This accepts a tuple containing the LEC and REC. Returns a string
    containg its accuracy.
    '''
    a = lecrec[1].split("/")
    b = int(a[1])
    if b >= 100000:
        return "Accuracy order: 1st Order Geodetic Control"
    
    elif b >= 50000 and b < 100000:
        return "Accuracy order: 2nd Order Geodetic Control"

    elif b >= 20000 and b < 50000:
        return "Accuracy order: 3rd Order Geodetic Control, Primary Project Control"

    elif b >= 10000  and b < 2000:
        return "Accuracy order: 4th Order Geodetic Control, Secondary Project Control"
    
    else:        
        return "Accuracy order: Tertiary Project Control"

def computeCorrCompass(dist,latdep):
    '''
    This function is used to compute the correction using Compass Rule. This accepts 
    a dictionary of the distance and its corresponding latitude and departure. Returns
    a dictionay with a valueof a list containting the corrected latitude and departure.
    Example. {1:[CorrLat,CorrDept]}
    '''
    t_dist = 0
    t_lat = 0
    t_dep = 0
    final = {}
    x = len(dist)+1
    for i in range(1,x):
        t_dist += dist[i]
        t_lat += latdep[i][0]
        t_dep += latdep[i][1]

    for i in range(1,x):
        #For latitudes computation
        corrCompLat = -(dist[i]/t_dist)*t_lat
        #For departure computation
        corrCompDep = -(dist[i]/t_dist)*t_dep
        final[i]=[corrCompLat,corrCompDep]

    return final

def computeCorrTransit(latdep):
    '''
    This function is used to compute the correction using Transit Rule. This accepts 
    a dictionary containing the latitude and departure of the lines. This returns a
    dictionay with a valueof a list containting the corrected latitude and departure.
    Example. {1:[CorrLat,CorrDept]}
    '''
    abs_lat = []
    abs_dep = []
    t_lat = 0
    t_dep = 0
    final = {}
    x = len(latdep)+ 1
    for i in range(1,x):
        abs_lat.append(abs(latdep[i][0])) #computing the absolute value of the lat
        abs_dep.append(abs(latdep[i][1])) #computing the absolute values of the dep
        t_lat += latdep[i][0] #computing the total lat
        t_dep += latdep[i][1] #computing the total dep
        
    t_abs_lat = math.fsum(abs_lat) #computing the total 
    t_abs_dep = math.fsum(abs_dep)
    
    for i in range(1,x):
        #For latitudes computation
        corrTransLat = -(abs_lat[i-1]/t_abs_lat)*t_lat
        #For latitudes computation
        corrTransDep = -(abs_dep[i-1]/t_abs_dep)*t_dep
        final[i]= [corrTransLat,corrTransDep]
        
    return final

def computeAdjLND(latdep,corrLND):#ayusing yung parameters and name
    '''
    This function is used to compute the adjusted latitude and departure of the traverse
    for it to close. This accepts two dictionaries containing the Latitude and Departure
    and the corrected Latitude and Departure. Returns a dictionary with a list for its
    value. The list contains the adjusted latitude and departure.
    Example {1:[adjLat,adjDep]}
    '''
    final ={}
    x = len(corrLND)+1
    for i in range(1,x):
        final[i]=[latdep[i][0]+corrLND[i][0],latdep[i][1]+corrLND[i][1]]

    return final

def computeAdjDistBear(adjComp):
    '''
    This function is used to compute the adjusted distance and bearing of the closed loop
    traverse. This accepts a dictionary containing a list of the adjusted latitude and
    departure. Returns a dictionary with list as its value. The list contains the
    adjusted distance and bearing. (Example. {1:[adjDist,adjBearing]}
    '''
    final = {}
    x = len(adjComp)+1
    for i in range(1,x):
        adj_dist = math.sqrt(adjComp[i][0]**2+adjComp[i][1]**2)
        angle = abs(math.atan((adjComp[i][1]/adjComp[i][0]))*(180/math.pi))
        DMS_deg = math.trunc(angle)
        raw_min = (angle - DMS_deg)*60
        DMS_min = math.trunc((angle - DMS_deg)*60)
        DMS_sec = (raw_min - DMS_min)*60
        dms_brng = f"{DMS_deg}-{DMS_min}-{DMS_sec:0.2f}"
        
        if adjComp[i][0] >= 0:
            if adjComp[i][1] >= 0:
                adj_brng = f"N {dms_brng} E"
            else:
                adj_brng = f"N {dms_brng} W"
        else:
            if adjComp[i][1] >= 0:
                adj_brng = f"S {dms_brng} E"
            else:
                adj_brng = f"S {dms_brng} W"
        
        final[i]=[adj_dist , adj_brng]
    return final

def computeAdjCoordinates(coordinates,adjComp):
    '''
    This function computes the ajdusted coordinates of each point in the closed loop
    traverse. This function accepts a dictionary for both the coordinates and adjusted
    latitude and departure. Returns a dictionary of list containg the Northing and
    Eastings. (Example. {1:[N,E]}
    '''
    x = len(adjComp)+1
    final={}
    n = coordinates[1][1]
    e = coordinates[1][0]
    for i in range(1,x):
        if i == 1:
            final[i]=[n,e]
        else:    
            n = n + adjComp[i-1][0]
            e = e+ adjComp[i-1][1]
            final[i]=[n,e]
    return  final

def areaDMD(adjComp):
    '''
    This function is used to compute the area of the polygon using DMD method. This
    will accept a dictionary containing the adjusted latitude and departure. This
    returns a dictionary of list containing the DMD and DPA. The last key contains the
    area in float type. (Example. {1:[DMD,DPA], ...., n: area})
    '''
    #initializing values
    dmd = []
    dpa=[]
    final = {}
    
    sum_dpa =0
    area = 0
    x=len(adjComp)+1
    #Computing for DMD
    dmd.append(adjComp[1][1])
    dmd_val = adjComp[1][1]

    for i in range(2,x):
        dmd_val = dmd_val + adjComp[i-1][1] + adjComp[i][1]
        dmd.append(dmd_val)

    for i in range(1,x):
        dpa.append(dmd[i-1]*adjComp[i][0])
    area = float(abs(math.fsum(dpa))/2)
    for i in range (1,x):
        final[i]= [dmd[i-1],dpa[i-1]]
    final[x] = area

    return final #{1:[DMD,DPA], ...., n: area}

#WAG MUNA TO OMGEEE
def printLECREC(lecrec,acc):
    '''
    This function prints the LEC, REC, and Accuracy order of the traverse. This accepts a
    a tuple containing the LEC and REC and a string containing the accuracy. No returns.
    '''
    print("---------------")
    print("ACCURACY CHECK")
    print("---------------")
    print(f"LEC: {lecrec[0]:0.3f} m")
    print(f"REC: {lecrec[1]}")
    print(acc)

def printAdj(given,corr,adj):
    '''
    This function prints the Tranverse Distance Computations. The function accepts three
    dictionary parameters. The first parameter contains the Name, Distance, Bearing,and
    Latitude and Departure. The second parameter has a value of list containing the
    correction latitude and departure. The last parameter contains the adjusted latitude
    and departure. No returns.
    '''
    #given {1: [NAME, DIST, BEARING, [LAT,DEP]]}
    #corr {1: [CORR LAT, CORR DEP]}
    #adj {1: [ADJ LAT, ADJ DEP]}
    print("---------------------------------")
    print("TRANSVERSE DISTANCE COMPUTATIONS")
    print("---------------------------------")
    print(f"{'Line':<5}|{'Distance':^10}|{'Bearing':^14}|{'Latitude':^10}|{'Departure':^12}|{'Corr_Lat':^10}|{'Corr_Dep':^10}|{'Adj_Lat':^10}|{'Adj_Dep':^10}")
    x = len(given) + 1
    for i in range(1,x):
        print(f"{given[i][0]:^5}|{given[i][1]:^10.3f}|{given[i][2]:^14}|{given[i][3][0]:^10.3f}|{given[i][3][1]:^12.3f}|{corr[i][0]:^10.5f}|{corr[i][1]:^10.5f}|{adj[i][0]:^10.3f}|{adj[i][1]:^10.3f}")
        
def printAdjDNB(name,adj):
    '''
    This function prints the adjusted distance and bearing. This accepts two dictionaries
    that contains the name and adjusted latitude and departure. No returns. 
    '''
    # adj = {1:[adjDist,adjBearing]}
    print("------------------------------")
    print("ADJUSTED DISTANCE AND BEARING")
    print("------------------------------")
    print(f"{'Line':<5}|{'Adj_Dist':^10}|{'Adj_Bearing':^17}")
    x = len(name) + 1
    for i in range (1,x):
         print(f"{name[i]:^5}|{adj[i][0]:^10.3f}|{adj[i][1]:^17}")

def printAdjCoordinates(name,adj):
    '''
    This function is used to print the adjusted coordinates. This accepts two dictionaries
    that contains the name and adjusted coordinates. No returns
    '''
    #adj = {1:[N,E]}
    #Finding the points of polygon
    point = {}
    x = len(name) + 1
    for i in range(1,x):
        a = name[i].split("-") #Spliting the line name using - # a is now a list
        point[i] = a[0]
    print("---------------------")
    print("ADJUSTED COORDINATES")
    print("---------------------")
    print(f"{'Point':<5}|{'Northing':^12}|{'Easting':^12}")
    for i in range (1,x):
        print(f"{point[i]:^5}|{adj[i][0]:^12.3f}|{adj[i][1]:^12.3f}")

def printAreaComp(name,adj,area): #adj latitude and departure
    '''
    This function is used to print the area computation. This requires 3 dictionary as
    parameters. The parameters needed are the name, adjusted latitude and departure, and
    the dictionary containg the DMD, DPA, and total area. No returns.
    '''
    #name = {1:"name"}
    #adj = {1:[lat,dep]}
    #area = {1:[DMD,DPA], ...., n: area})
    point = {}
    x = len(name) + 1
    for i in range(1,x):
        a = name[i].split("-") #Spliting the dms using - # List na yarn 
        point[i] = a[0]
    poly_name = ""
    for i in range (1,x):
        poly_name += point[i]
    print("-----------------")
    print("AREA COMPUTATION")
    print("-----------------")
    print(f"{'Line':<5}|{'Adj_Lat':^12}|{'Adj_Dep':^12}|{'DMD':^12}|{'DPA':^14}")
    for i in range (1,x):
        print(f"{name[i]:^5}|{adj[i][0]:^12.3f}|{adj[i][1]:^12.3f}|{area[i][0]:^12.3f}|{area[i][1]:^14.3f}")
    print()
    print(f"The area of the traverse polygon {poly_name} is {area[x]:0.3f} square meters")
        
    
    
        
    
    


        
        
        
        
    


