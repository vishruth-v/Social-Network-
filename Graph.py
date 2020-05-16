class Graph:
    def __init__(self, nodes, names):
        self.adjlist = [[] for i in range(nodes)]
        self.indexes = {i:j for i,j in zip(names, range(nodes))}
        self.V = nodes #V is th number of nodes present in the graph
        self.cycle = []
    
    def disp_adjlist(self):
        print(self.adjlist)
    
    def disp_indexes(self):
        print(self.indexes)
    
    def display(self):
        print(self.adjlist)
        print(self.indexes)
        print(self.V)
        
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
        else:
            print("Invalid connection")
            
    '''def addmult(self, n):
        for _ in range(n):
            self.indexes.update({chr(len(self.adjlist)+65): len(self.adjlist)})
            self.adjlist.append([])'''
    
    def add(self, name):
        self.indexes.update({name: len(self.adjlist)})
        self.adjlist.append([])
        self.V += 1


    def delete(self,node):
        index = self.indexes[node]
        self.indexes.pop(node)
        for i in self.adjlist[index]:
            self.adjlist[self.indexes[i]].remove(node)
        self.adjlist.pop(index)
        for x in self.indexes:
            if self.indexes[x] > index:
                self.indexes[x] -= 1
        self.V -= 1
    '''
    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v 
    def isCyclicUtil(self,start_node,visited,parent): 
        startcycle = None
        l = []
        #Mark the current node as visited  
        visited[start_node]= True
  
        #Recur for all the vertices adjacent to this vertex (adjacency list of that vertex) 
        for node in self.adjlist[self.indexes[start_node]]: 
            # If the node is not visited then recurse on it 
            if  visited[node]==False :  
                if(self.isCyclicUtil(node,visited,start_node)[0]) and start_node != startcycle: 
                    return True,l.append(start_node)
                elif(self.isCyclicUtil(node,visited,start_node)[0]) and start_node == startcycle:
                    return True,l
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif (visited[node]==True and parent != node): 
                startcycle = node
                l = [start_node]
                return True, l
          
        return False,l
    
    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        #visited =[False]*(self.V)
        visited = {name : False for name in self.indexes} 
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for node in self.indexes: 
            if visited[node] == False: #Don't recur for u if it is already visited
                #b, l = self.isCyclicUtil(node,visited,-1)
                #if b == True: 
                if(self.isCyclicUtil(node,visited,-1))[0] == True: #initial parent node = -1 
                    print(l)
                    return True,l
        return False,l
        '''
    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v. 
    def isCyclicUtil(self,start_node,visited,parent): 
  
        #Mark the current node as visited  
        visited[start_node]= True
  
        #Recur for all the vertices adjacent to this vertex 
        for node in self.adjlist[self.indexes[start_node]]: 
            # If the node is not visited then recurse on it 
            #self.cycle.append(start_node) 
            if  visited[node]==False:  
                if(self.isCyclicUtil(node,visited,start_node)[0]): 
                    self.cycle.append(start_node)
                    return True, self.cycle
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=node:
                self.cycle.append(start_node)
                return True, self.cycle
        if self.cycle:
            self.cycle.pop()
        return False, self.cycle

    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        visited = {name : False for name in self.indexes}
         
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for node in self.indexes: 
            if visited[node] ==False: #Don't recur for u if it is already visited 
                b, self.cycle = self.isCyclicUtil(node,visited,-1)
                if b == True: 
                    return True
        
        return False, self.cycle

    def popularity(self):
        name_index = {v: k for k, v in self.indexes.items()}
        popu_dict = {name_index[i]: len(self.adjlist[i]) for i in range(len(self.adjlist))}
        return sorted(list(popu_dict.items()), key=lambda x: x[1], reverse=True)

    # Suggests top friends
    def suggested(self, name):
        node = self.indexes[name]
        children = [self.indexes[n] for n in self.adjlist[node]]
        con = {}
        for child in children:
            grandchildren = self.adjlist[child]
 
            # List of names
            for gc in grandchildren:
                if self.indexes[gc] in children or gc == name:
                    continue
                # If connection exists
                if gc in con.keys():
                    con[gc] += 1
                # Initialise to 1
                else:
                    con[gc] = 1
       
        con = sorted(list(con.items()), key=lambda x:x[1], reverse=True)
       
        return con
    

'''if __name__ == '__main__':
    #Testing of the class for add delete
    g1 = Graph(2, ['Vish', 'Vibhz'])
    g1.display()
    g1.connect('Vish', 'Vibhz')
    g1.display()
    g1.add('Cool')
    g1.display()
    g1.delete('Vibhz')
    g1.display()
    g1.add('Bruh')
    g1.display()'''

if __name__ == '__main__':
    g1 = Graph(5, ['A', 'B', 'C', 'D', 'E'])
    #g1.display()
    g1.connect('E', 'D')
    g1.connect('D', 'A')
    g1.connect('A', 'B')
    g1.connect('B', 'C')
    g1.connect('C', 'D')
    g1.display()
    print(g1.cycle)
    print(g1.isCyclic())
    

    
