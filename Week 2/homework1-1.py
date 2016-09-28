from __future__ import division

dragons =  ({(x,y):(x**2 + y**2) if x in (1,2,4) and y in (1,3) else 0 for x in range(1,5) for y in range(1,4)})

total = 0
yltx = 0
xlty = 0
xequalsy = 0
yequals = 0

px = {key: 0 for key in range(1,5)}
py = {key: 0 for key in range(1,4)}

for i,v in dragons.items():
    total += v
    
    if i[1]<i[0]: #if Y < X
        yltx += v/72
    if i[0]<i[1]: #if X < Y
        xlty += v/72
    if i[0]==i[1]: #if X = Y
        xequalsy += v/72
    if i[1]==3: #if Y = 3
        yequals += v/72
        
    for w in range(1,5): #Recorro el rango de X, y si X == x, sumo el valor al diccionario
        if i[0] == w:
            px[w] += v/72
            
    for z in range(1,4): #Recorro el rango de Y, y si Y == y, sumo el valor al diccionario
        if i[1] == z:
            py[z] += v/72
  
        
