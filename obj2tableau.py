# Convert an OBJ file (a 3D Object Format - examples at https://people.sc.fsu.edu/~jburkardt/data/obj/obj.html)
# into a CSV file for Tableau to ingest
# so the 3D object can be displayed in Tableau. The columns for the CSV file are
# the X, Y, Z coordinates of vertex points, and a number indicating a particular
# edge id of the object. Each edge is defined by the two rows in the columns that share
# the same edge id.
# The use of this is explained on https://pinpointuncertainty.blogspot.com/2013/11/your-own-3d-rotatable-cow.html
# where there is an exampled of wireframe cow rotatable in Tableau.

import sys

def print_line(vertex, edge):
    sys.stdout.write(('%s, %s, %s, "%d"\n') % (vertex[0], vertex[1], vertex[2], edge))


# Column names
print("X, Y, Z, Edge")

lineNum = 0
doneWithV = False
faces = []
vertices = [[]]

f = open(sys.argv[1])

for line in f:
    lineNum += 1
    line = line.rstrip('#')
    line = line.strip()
    if len(line) == 0:
        continue
    vals = line.split()
    if vals[0] == 'v':
        if doneWithV:
            print("V after F")
            sys.exit(0)
        if len(vals) != 4:
            print("Invalid line #", lineNum)
            continue
        vertices.append(vals[1:])

    elif vals[0] == 'f':
        doneWithV = True
        faces.append(vals[1:])

edge = 0
for face in faces:

    # Add the first vertex to the end of the list of vertices
    # so there is a line from the last to the first vertex.

    face += [face[0]]

    for i in range(len(face) - 1):
        print_line(vertices[int(face[i])], edge)
        print_line(vertices[int(face[i + 1])], edge)
        edge += 1;
