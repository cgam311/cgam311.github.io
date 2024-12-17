# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 May 13
# Machine Exercise 4

def getCoordinates():
    '''
    This function is used to read the text file. This function shall assign the coordinates
    in a tuple (X,Y). This accepts no argument. Returns a dictionary containing the points
    from the file.
    '''
    try:
        f = open("Points.txt")
        x = f.readlines()
        coord = {}
        if len(x)<=3: #kasi less than 3 ibigsabihn title bar + 2 points lang
            raise Exception("ERROR: Less than 3 points provided") 
        for data in x:
            sep = data.split("\t")#hiwalay gamit \t
            if len(sep)!=3:
                raise Exception("ERROR: Wrong format of points")
            if sep[0] == "Point":
                continue
            else:
                coord[sep[0]]=(float(sep[2].replace("\n","")),float(sep[1])) 
        f.close()
        return coord
    except FileNotFoundError: 
        print("ERROR: File not found") 
    except Exception as e:
        print(e)
    except Exception as f:
        print(f)
    
def areaDMD(dictionary): #palitan ng str yung key
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
        lat_val = dictionary[str(i+1)][1] - dictionary[str(i)][1]#Computation of lat except from last line
        lat.append(lat_val)#Append to lat list

    lat_val = dictionary[str(1)][1] - dictionary[str(x)][1] #Computation of lat of the closing line
    lat.append(lat_val)#Append to lat list

    for i in range(1,x):
        dep_val = dictionary[str(i+1)][0] - dictionary[str(i)][0]#Computation of dep except from last line
        dep.append(dep_val)#Append to lat list

    dep_val = dictionary[str(1)][0] - dictionary[str(x)][0]#Computation of dep of the closing line
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

def writeArea(dictionary,area):
    '''
    This fucntion re-writes the arguments in to a new text file with a filename:MACAM_Area.txt
    This accepts a dictionary containing the points of a polygon and this also accepts an area
    computed beforehand. Returns none.
    '''
    x = len(dictionary)
    a = []
    f = open("MACAM_Area.txt","w+")
    string ="Point\tNorthings\tEastings\n" #para sa title part
    f.write(string) #sulat yung title part
    for i in range(1,x+1):
        nort=dictionary[str(i)][1] #data para sa northings
        east=dictionary[str(i)][0]  #data para sa eastings
        a.append(f"{i}\t{nort:0.3f}\t{east:0.3f}\n")
    f.writelines(a) #sulat data ng points
    final_area= f"\nThe area computed is {area:0.3f} square units"
    f.write(final_area)#sulat ng area

while True:
    try:
        coord=getCoordinates()
        area = areaDMD(coord)
        writeArea(coord,area)
    except: #para kung mag error, stop na agad
        break
    else: #naka true yung while para magstop hehe
        break

        

    
    

