class Graph:
    def __init__(self, nodes, names):
        self.adjlist = [[] for i in range(nodes)]
        self.indexes = {i:j for i,j in zip(names, range(nodes))}
    
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
        else:
            print("Invalid connection")
            
    def addmult(self, n):
        for _ in range(n):
            self.indexes.update({chr(len(self.adjlist)+65): len(self.adjlist)})
            self.adjlist.append([])
    
    def add(self, name):
        self.indexes.update({name: len(self.adjlist)})
        self.adjlist.append([])


    def delete(self,node):
        index = self.indexes[node]
        self.indexes.pop(node)
        for i in self.adjlist[index]:
            self.adjlist[self.indexes[i]].remove(node)
        self.adjlist.pop(index)
        for x in self.indexes:
            if self.indexes[x] > index:
                self.indexes[x] -= 1

if __name__ == '__main__':
    '''Testing of the class'''
    g1 = Graph(2, ['Vish', 'Vibhz'])
    g1.display()
    g1.connect('Vish', 'Vibhz')
    g1.display()
    g1.add('Cool')
    g1.display()
    g1.delete('Vibhz')
    g1.display()
    g1.add('Bruh')
    g1.display()