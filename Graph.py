class Graph:
    def __init__(self, nodes):
        self.adjlist = [[] for i in range(nodes)]
        self.indexes = {chr(i+65):i for i in range(nodes)}
    
    def disp_adjlist(self):
        print(self.adjlist)
    
    def disp_indexes(self):
        print(self.indexes)
    
    def display(self):
        print(self.adjlist)
        print(self.indexes)
        
    def isValid(self, node):
        if node in self.indexes:
            return 1
        else:
            return 0
        
    def connect(self, node1, node2):
        if self.isValid(node1) and self.isValid(node2):
            if node2 not in self.adjlist[self.indexes[node1]]:
                self.adjlist[self.indexes[node1]].append(node2)
                self.adjlist[self.indexes[node2]].append(node1)
            #print(adj_list)
        else:
            print("Invalid connection")
            
    def add(self, n):
    #n = int(input("Enter no. of nodes to be added:"))
        for _ in range(n):
            self.indexes.update({chr(len(self.adjlist)+65): len(self.adjlist)})
            self.adjlist.append([])
        #print(adj_list)
        #print(indexes)
    
    def delete(self,node):
        index = self.indexes[node]
        self.indexes.pop(node)
        for i in self.adjlist[index]:
            self.adjlist[self.indexes[i]].remove(node)
        self.adjlist.pop(index)
        #print(indexes)
        #print(adj_list)