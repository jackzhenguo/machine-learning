"""
Dijkstra algorithm
graphdict={"A":[("B",6),("C",3)], "B":[("C",2),("D",5)],"C":[("B",2),("D",3),("E",4)],\
         "D":[("B",5),("C",3),("E",2),("F",3)],"E":[("C",4),("D",2),("F",5)],"F":[("D",3),"(E",5)]})
assert: start node must be zero in-degree
"""

def Dijkstra(startNode, endNode, graphdict=None):
    S=[startNode]
    V=[]
    for node in graphdict.keys():
        if node !=startNode:
            V.append(node)
    #distance dict from startNode
    dist={}
    for node in V:
        dist[node]=float('Inf')

    while len(V)>0:
        center = S[-1] # get final node for S as the new center node
        minval = ("None",float("Inf"))
        for node,d in graphdict[center]:
            if node not in V:
                continue
            #following is the key logic.If S length big than 1,need to get the final ele of S, which is the center point in current
            #iterator, and distance between start node and center node is startToCenterDist; d is distance between node
            # among out-degree for center point; dist[node] is previous distance to start node, possibly Inf or a updated value
            # so if startToCenterDist+d is less than dist[node], then it shows we find a shorter distance.
            if len(S)==1:
                dist[node] = d
            else:
                startToCenterDist = dist[center]
                if startToCenterDist + d < dist[node]:
                    dist[node] = startToCenterDist + d
            #this is the method to find a new center node and
            # it's the minimum distance among out-degree nodes for center node
            if d < minval[1]:
                minval = (node,d)
        V.remove(minval[0])
        S.append(minval[0]) # append node with min val
    return dist


shortestRoad = Dijkstra("A","F",graphdict={"A":[("B",6),("C",3)], "B":[("C",2),("D",5)],\
                            "C":[("B",2),("D",3),("E",4)],\
                            "D":[("B",5),("C",3),("E",2),("F",3)],\
                            "E":[("C",4),("D",2),("F",5)],"F":[("D",3),("E",5)]})

mystr = "shortest distance from A begins to "
for key,shortest in shortestRoad.items():
    print(mystr+ str(key) +" is: " + str(shortest) )

