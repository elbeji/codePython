import networkx as nx
import matplot.pyplot as plt



#define a graph
G=nx.Graph()




#read file data
readfile=open("c:\autoexec.bat","r")
for line in readfile:
    spline=line.split(",")
    if(int(spline[2]):
       G.add_edge(spline[0],spline[1],color='r')
    print(line)
    G.add_edge(spline[0],spline[1],color='b')

pos=nx.circular_layout(G)
edges=G.edges()
colors=[G[u],[v]['color'] for u,v in edges]
nx.draw(G,pos,node_color='b',with_label='True',edges=edges,edge_color=colors)
plt.show()
    
