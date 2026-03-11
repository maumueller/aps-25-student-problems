import sys
import re


line = sys.stdin.readline()

if line == "": #If input file is empty
    print("Error: Input must not be empty")
    sys.exit(43)

if(line.startswith('0')): #Checks if nr of spacestations is 0
    print("Error: nr of spacestations cannot be 0")
    sys.exit(43)

try: #checks if the intput can be converted to an int
    nrStations = int(line)
    if not 1 <= nrStations <= 100:
        print("Error: nr of spacestations out of bounds")
        sys.exit(43)
except ValueError:
    print("Error: nr of spacestations must be an integer")
    sys.exit(43)


for _ in range(nrStations):
    spaceStation = sys.stdin.readline().split() 
    if len(spaceStation) != 3: #if the spacestatioon does not have x, y and z
        print("Error: a spacestation must consist of x,y,z coordinates")
        sys.exit(43)

    for i in range (len(spaceStation)):
        if spaceStation[i] == "": #if no coordinate
            print("Error: coordinate must not be empty")
            sys.exit(43)

        if len(spaceStation[i]) > 1: #check for leading and trailing zeroes, if the length is greater than 1
            if(spaceStation[i].startswith('0') and spaceStation[i][1] != '.'): #if the coordinate start with 0 and the following character is not a dot.
                print("Error: starting character '0', must be followed by a '.'")
                sys.exit(43)
            if '.' in spaceStation[i] and spaceStation[i].endswith('0'): #if a dot exists and the last digit is 0
                print("Error: coordinate can't end with 0, if it is a float")
                sys.exit(43)

        try: #Check if coordinate can be cast to a float
            Coord = float(spaceStation[i])

            if i == 0: #constraints for x
                if not 1.0 <= Coord <= 100.0: #spacestation can not be located in 0.0 and must be positive
                    print("Error: x coordinate is out of bounds")
                    sys.exit(43)

            elif not -100.0 <= Coord <= 100.0: #constraints for y and z 
                print("Error: y or z coordinate is out of bounds")
                sys.exit(43)

        except ValueError:
            print("Error: Coord must be a float")
            sys.exit(43)

#Checks if there is more input than what we expect
if sys.stdin.readline() != "":
    print("Error: Too much input")
    sys.exit(43)

sys.exit(42)

