class Node():
    def __init__(self, val, arr):
        self.left = None
        self.right = None
        self.val = val
        self.arr = arr
    
    def insert(self, val, arr):
        if self.val: 
            if val < self.val:
                if self.left is None:
                    self.left = Node(val, arr)
                else:
                    self.left.insert(val, arr)
            else:
                if self.right is None:
                    self.right = Node(val, arr)
                else:
                    self.right.insert(val, arr)
        else:
            self.data = data
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print("Array = ", self.arr, "Gap= ",self.val)
        if self.right:
            self.right.printtree()
    
    def inorderTraversal(self, root):
        res =[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append("{ gap= "+str(root.val)+ ", array=("+ str(root.arr)+")}")
            res = res + self.inorderTraversal(root.right)
        return res
    
    def depth(self):
        current_depth = 0
        
        if self.left:
            current_depth = max(current_depth, self.left.depth())
        if self.right:
            current_depth = max(current_depth, self.right.depth())

        return current_depth + 1
    
    def minValue(self,node):
        current = node

        while(current.left is not None):
            current = current.left
        return current.arr
                    

def calculateArray(A,B,k):
    B=sorted(B)
    w=len(A)
    h=len(B)
    for i in range(w):
        for j in range(h):
            if i == 0 and j == 0:
                root = Node(abs(A[i]+B[j]-k), str(A[i])+", "+str(B[j]))
            else:
                root.insert(abs(A[i]+B[j]-k), str(A[i])+", "+str(B[j]))
    print(root.inorderTraversal(root))
    print("depth = ", root.depth())

    print("Closest possible pair: ",root.minValue(root))

A = [6, 7, 5, 4]
B = [1, 1, 8, 2]
k = 10
calculateArray(A,B,k)

