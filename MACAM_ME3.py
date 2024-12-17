# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 March 28
# Machine Exercise 3

#Defining the different functions needed

def getCoordinate(): 
    '''
    This function ask for a coordinates in a string format of X,Y (Example 20000,20000).
    The function will continue to ask for coordinates unless the keyword 'END' is entered.
    There are no arguments to be entered to the function. Returns a dictionary with keys
    as coordinate numbers and values of an tuple coordinate pair.
    '''
    crd = "get" #Initializing values
    num = 1 #Coordinate Number
    crd_dict ={}
    while crd != "END":
        crd = input(f"Enter coordinate {num}: ")
        if crd != "END" :
            crd_t = tuple(float(pt) for pt in (crd.split(',')))
            crd_dict[num] = crd_t #Adding the value to the dictionary
            num += 1
        else:
            return crd_dict

def printCoordinates(dictionary):
    '''
    This function will print the a summary of the coordinates in the format of Point Number,
    Northing, Easting. This will accept a dictionary value. No returns.
    '''
    x = len(dictionary) + 1 # 3 values in dict = 3 len; +1 for the range
    print(f"{'Point':<5}{'Northing':^15}{'Easting':>8}")
    for i in range(1,x):# if 3 values in dict => range (1,4) => values 1 to 3 
        print(f"{i:<5}{dictionary[i][1]:^15.3f}{dictionary[i][0]:>10.3f}")

def askMethod():
    '''
    This funtion will ask for the type of area computation to be performed. It has 2 choices
    DMD method or Coordinate method. The keywords are "DMD" or "dmd" for DMD method and
    "Coordinate" or "coordinate" for Coordinate method. This will continue to ask for a
    method unless the accepted keyword is indicated. There are no values accepted on
    the arguments. This function returns a string of the indicated method accepted.
    '''
    ask = "initial"
    while not(ask == "DMD" or ask == "dmd" or ask == "Coordinate" or ask == "coordinate"):
        ask = input("Method for Area Computation (DMD/Coordimate): ")

    if ask == "DMD" or "dmd":
        return ask
    else:
        return ask

def areaCoord(dictionary):
    '''
    This function is used to compute the area of the polygon using Coordinate method. This
    will accept a dictionary type of values to perform the computation. This returns the area
    computed in float type.
    '''
    #Initializing values
    x = len(dictionary) 
    up = 0
    down = 0
    
    #Computing downards
    for i in range (1,x):
        down += dictionary[i][0]*dictionary[i+1][1] #Final coordinate not included in this loop
    down += dictionary[x][0]*dictionary[1][1] #Final coordinate
    
    #Computing upwards
    for i in range (1,x):
        up += dictionary[i][1]*dictionary[i+1][0] #Final coordinate not included in this loop
    up += dictionary[x][1]*dictionary[1][0] #Final coordinate
    
    area = float(0.5 * (abs(down-up)))
    return area


def areaDMD(dictionary):
    '''
    This function is used to compute the area of the polygon using DMD method. This will
    accept a dictionary type of values to perform the computation. This returns the area
    computed in float type.
    '''
    #Initializing values
    x = len(dictionary)
    lat=[]
    dep=[]
    dmd=[]
    dpa=[]
    sum_dpa = 0
    #Computing the Lat and Dep of the values

    for i in range(1,x): 
        lat_val = dictionary[i+1][1] - dictionary[i][1]#Computation of lat except from last line
        lat.append(lat_val)#Append to lat list

    lat_val = dictionary[1][1] - dictionary[x][1] #Computation of lat of the closing line
    lat.append(lat_val)#Append to lat list

    for i in range(1,x):
        dep_val = dictionary[i+1][0] - dictionary[i][0]#Computation of dep except from last line
        dep.append(dep_val)#Append to lat list

    dep_val = dictionary[1][0] - dictionary[x][0]#Computation of dep of the closing line
    dep.append(dep_val)#Append to lat list

    #Computing for DMD

    #First dmd
    dmd.append(dep[0]) #copy value sa una tas append sya sa dmd list
    dmd_val = dep[0] #Assign value sa una

    #DMD hanggang sa dulo
    for i in range(1,x):
        dmd_val= dmd_val + dep[(i-1)] + dep[(i)] 
        dmd.append(dmd_val)#Append to dmd list

    #Computing for DPA values    
    for i in range(x):
        dpa_val = dmd[i] * lat [i]
        dpa.append(dpa_val)#Append to dpa list

    for i in range(x):
        sum_dpa += dpa[i]
        
    area = float(0.5 * (abs(sum_dpa)))
    return area

crd = getCoordinate() #Getting values for a dictionary
print("")
printCoordinates(crd) #Printing the dictionary
print("")
met = askMethod() #String for the method
print("")

#Checking the string for the method 
if met == "DMD" or met =="dmd":
    area = areaDMD(crd)
    print("Method of Area Computation: Double Meridian Method")
    print(f"The area is {area:0.3f} square units")    
else:
    area = areaCoord(crd)
    print("Method of Area Computation: Coordinate Method")
    print(f"The area is {area:0.3f} square units")

            
