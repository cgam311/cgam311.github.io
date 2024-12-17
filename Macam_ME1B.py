# MACAM, Christina Gianne A. (2019-05712) - Python 3.9.1 - 2022 March 01
# Machine Exercise 1 Part 2: Quadratic Equations

raw = input("Enter quadratic equation: ")

# Using the general form ax^2+bx+c=0 separate the variables
# no signs included just integers first

a = str(int(raw[0:3]))
b = str(int(raw[7:10]))
c = str(int(raw[12:15]))

# Include signs for the variables 'b' and 'c'
# Convert the strings to integers/float

a = float(a)
b = float(raw[6] + b)
c = float(raw[11] + c)

# These are the final variables to be used in the quadratic equation.

# The quadratic formula is [-b +/- sqrt(b^2-4ac)]/2a
# Separate the discriminant and denominator part

disc = ((b**2) - (4 * a * c))**0.5
den = 2 * a

# Rewrite the numerator, either using + or - sign

pos_num = -b + disc
neg_num = - b - disc

# Combine to make the fractions for the different roots

root_1 = pos_num / den
root_2 = neg_num / den

# Print the solution/roots of the equation

print("The roots of the quadratic equation {0} are".format(raw), end=" ")
print("{0:1.3f} and {1:1.3f}".format(root_1, root_2))
