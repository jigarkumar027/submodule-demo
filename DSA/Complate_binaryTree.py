
class Node:
    def __init__(self,val) -> None:
        self.root = val
        self.left = None
        self.right = None

def count_Node(node):
    if node == None:
        return 0
    return (1 + count_Node(node.left) + count_Node(node.right))

def check_CBT(node,index,Noofele):
    if node is None:
        return True
    if index >= Noofele:
        return False
    return check_CBT(node.left,2*index+1,Noofele ) and check_CBT(node.right,2*index+2,Noofele)

CBT = Node(5)
CBT.left = Node(2)
CBT.right = Node(3)
CBT.left.left = Node(6)
CBT.left.right = Node(7)
CBT.right.left = Node(9)
CBT.right.right = Node(99)


count = count_Node(CBT) 
print(count)  
print(check_CBT(CBT,0,count))