
"""
prim algorithm to get minimal spanning tree
adj:adjacent matrix
"""

def primToMST(adj,startPoint="A"):
    indexdict = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
    citydict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
    vnew=[startPoint]
    edge=[]
    sum=0
    #vnew
    edg=[] #element is cell, eg. (u,v)
    while len(vnew)<len(citydict):
        imin = (-1,float('Inf'))
        centerCity=""
        for city in vnew:
            cur = citydict[city]-1
            ws = adj[cur]
            for (i,w) in enumerate(ws):
                if indexdict[i+1] not in vnew and 0 < w and  w < imin[1]:
                    imin = (i+1,w)
                    centerCity=city
        vnew.append(indexdict[imin[0]]) #add the city with minimum weight
        edge.append((centerCity,indexdict[imin[0]]))
        sum+=imin[1]
    return sum,vnew,edge



sum,vnew,edges =primToMST([ [0,7,0,5,0,0,0],
                           [7,0,8,9,7,0,0],
                           [0,8,0,0,5,0,0],
                           [5,9,0,0,15,6,0],
                           [0,7,5,15,0,8,9],
                           [0,0,0,6,8,0,11],
                           [0,0,0,0,9,11,0]],startPoint="D")

print("weight sum: "+str(sum))
print("vertex:")
[print(city) for city in vnew]
print("edge: ")
[print("("+str(v)+","+str(u)+")")for (v,u) in edges]
