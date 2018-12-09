"""
ID: alex.go2
LANG: PYTHON3
TASK: gift1
"""
import math
f = open('comp2.txt', 'r')
g = open('gift1.out', 'w')
readfile = f.readlines()
"""y is basically on which line we are on"""
numofpeople = int(readfile[0])
y = numofpeople + 2
listofpeople = []
for x in range (0, numofpeople):
    listofpeople.append([readfile[x+1], 0])
for q in range(0, len(readfile)):
    if y < len(readfile)-1:
        howmuch = int(readfile[y][:-3])
        howmany = int(readfile[y][-3:-1])
        print(howmany)
        for c in range(0, len(listofpeople)):
            if readfile[y - 1] == listofpeople[c][0]:
                if howmany != 0:
                    listofpeople[c][1] = listofpeople[c][1] - howmuch + howmuch % howmany
       
        for x in range(0,int(howmany)):
            for z in range(0, len(listofpeople)):
              
                if listofpeople[z][0] == readfile[x+y+1]:
                    listofpeople[z][1] = listofpeople[z][1] + math.floor(howmuch/howmany)
                   
        y = y + int(howmany) + 2
       

for b in range (0, len(listofpeople)):
    g.write(str(listofpeople[b][0][0:-1]))
    g.write(" " + str(listofpeople[b][1]) + "\n")
     

g.close()
       


            
    


