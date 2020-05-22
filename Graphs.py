# Graphs has vertices and edges lets see How we can depect them using python
# V  = vertices
# E = Edges
#--------------------------------------#--------------------------------------#
# V = {'a','b','c','d','e'}
# E = {'ab','ac','bd','cd','de'}

#create the dictionary as graph

# graph = {
#     'a':['b','c'],
#     'b': ['a','d'],
#     'c':['d','a'],
#     'd':['e'],
#     'e':['d']
# }
# print(graph)

#-----------------------------------------#------------------------------------#

# Display the graph Vertices

# class graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict= []
#         self.gdict =gdict


# # get the keys of the dictionary
#     def getVetices(self):
#         return list(self.gdict.keys())


# # create a graph

# graph_elements = {
#     'a':['b','c'],
#     'b': ['a','d'],
#     'c':['d','a'],
#     'd':['e'],
#     'e':['d']
# }
# g =graph(graph_elements)
# print(g.getVetices())

#-----------------------------------------#------------------------------------#

#get graph edges


# class graph:
#     def __init__(self,gdict= None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict


#     def edges(self):
#         return self.findedges()

# # now we have to find the edges the code is below


#     def findedges(self):
#         edgenames = []
#         for vertex in self.gdict:
#             for nextVertex in self.gdict[vertex]:
#                 if {nextVertex,vertex} not in edgenames:
#                     edgenames.append({vertex,nextVertex})
#         return edgenames



# # create a graph

# graph_elements = {
#     'a':['b','c'],
#     'b': ['a','d'],
#     'c':['d','a'],
#     'd':['e'],
#     'e':['d']
# }
# g = graph(graph_elements)
# print(g.edges())

#-----------------------------------------#------------------------------------#


