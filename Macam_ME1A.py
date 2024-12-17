# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 March 01
# Machine Exercise 1 Part 1: Angle Conversions

import math

raw = float(input("Enter angle in Decimal Degree: "))
print("")
# Convert first the raw decimal degree to the range [0,360]

deg = raw % 360

# Print Input degree
print("Input: {0}".format(deg))

# Convert the deg to DMS form

DMS_deg = math.trunc(deg)
raw_min = (deg - DMS_deg)*60
DMS_min = math.trunc((deg - DMS_deg)*60)
DMS_sec = (raw_min - DMS_min)*60

# Print DMS
print("DMS: {} deg {} min".format(DMS_deg, DMS_min), end=" ")
print("{0:1.2f} sec".format(DMS_sec))

# Convert the deg to radians
# Deg * 180/pi
# 6 decimal places

rad = (deg *math.pi)/180

# Print radians
print("Radians: {0:1.6f} rad".format(rad))

# Convert radians to gradians
# 2pi = 400gradians

raw_g = rad*(200 / math.pi)
fin_g = math.trunc(raw_g)
raw_c = (raw_g-fin_g)*100
fin_c = math.trunc(raw_c)
fin_cc = (raw_c-fin_c)*100

# Print Gradians
print("Gradians: {} g {} c".format(fin_g, fin_c), end=" ")
print("{0:1.2f} cc".format(fin_cc))

# Convert gradians to mils
# 400 grads = 6400 mils or 1 grads = 16 mils

mils = raw_g * 16

# Print Mils
print("Mils: {0:1.6f} mils".format(mils))











