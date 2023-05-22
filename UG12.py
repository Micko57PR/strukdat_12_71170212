class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
    
class Tree:
    def __init__(self,root):
        self.root = root
    
    def addChild(self, node_parent, data):
        new_node = Node(data)
        new_node.parent = node_parent
        node_parent.child.append(new_node)
        return new_node

    
    def sums(self,node):
        sum = 0
        if len(node.child) == 0:
            return node.data
        for child in node.child :
            sum += self.sums(child)
        return sum + node.data
    
    def sibling(self,node):
        if len(node.parent.child) == 0:
            return node.data
        elif len(node.parent.child) == 1:
            return node.data
        else:
            sib = 0
            for child in node.parent.child:
                sib += child.data
            return sib
        
    
val200 = Node(200)
t = Tree(val200)

val23 = t.addChild(val200, 23) 
val11 = t.addChild(val200, 11)
val13 = t.addChild(val23, 13) 
val57 = t.addChild(val23, 57) 
val32 = t.addChild(val11, 32) 
val42 = t.addChild(val13, 42) 
val51 = t.addChild(val13, 51) 
val71 = t.addChild(val13, 71) 
val12 = t.addChild(val57, 12) 
val15 = t.addChild(val57, 15)
val33 = t.addChild(val32, 33)
val8 = t.addChild(val32, 8)


#test 1
print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')
 
#test 2
print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')