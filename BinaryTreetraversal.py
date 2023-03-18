# Complete Binary Tree - Every level must be completely filled, Leaf node is at left (max).
# Perfect Binary Tree - All Internal Node Degree is equal to 2, Leaf Nodes at same level.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def preorder(root):
    # (Logic starts from the main root/root node, down to left child node until it reaches the left leaf node, then proceeds to the right node)
    # (Logic: Root -> Left -> Right)
    # Iterative Approach
    if root:
        """
        - Recursive Approach

        print(root.data, end = " -> ")
        preorder(root.left)
        preorder(root.right) 

        """
        # Iterative Approach
        istack = []
        istack.append(root)

        while len(istack) > 0:
            node = istack.pop()
            print(node.data, end = " ")

            if node.right:
                istack.append(node.right)
            if node.left:
                istack.append(node.left)
    else:
        return

def inorder(root):
    # (Logic starts from the left subtree: Left -> Root -> Right)
    # - Recursive Approach

    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
        
    """    
     - Iterative Approach
    # you have to import deque first.
    # create an empty stack
    stack = deque()
    # start from the root node (set current node to the root node)
    curr = root
    # if the current node is None and the stack is also empty, we are done
    while stack or curr:
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            print(curr.data, end=' ')
 
            curr = curr.right
            """

def postorder(root):
    # (Logic start from left leaf node then right then root)
    # (Logic: Left -> Right -> Root)
    # Recursive Approach
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)

# Print nodes at a given level
def printGivenLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data,end=" ")
	elif level > 1 :
		printGivenLevel(root.left , level - 1)
		printGivenLevel(root.right , level - 1)
        
def height(node):
	if node is None:
		return 0
	else :
		# Compute the height of each subtree 
		leftheight = height(node.left)
		rightheight = height(node.right)

		#Use the larger one
		if leftheight > rightheight :
			return leftheight + 1
		else:
			return rightheight + 1

root = Node(5)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(8)

inorder(root)
preorder(root)
postorder(root)
printLevelOrder(root)