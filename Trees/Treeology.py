"""
CODE: TREE_O_LOGY
"""
from BinaryTree import BinaryTree

"""
                                                1
                        ┌───────────────────────┴───────────────────────┐
                        2                                               3
            ┌───────────┴───────────┐                       ┌───────────┴───────────┐
            4                       5                       6                       7
      ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐
      8           9          10          11          12          13          14          15
   ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐
  16    17    18    19    20    21    22    23    24    25    26    27    28    29    30    31

My TREE_O_LOGY:

>> Types of Binary Trees Arranged in order of symmetrical appearance with small info:
                            Most Symmetric to Least Symmetric

NULL / Empty Binary Tree:
    - A Binary Tree with no root node / NULL node
    - A Binary Tree whose leaf Nodes have NULL value
>> Height = NULL
>> Total Nodes = 0

Examples:
"""
print(BinaryTree(),
      BinaryTree([]),
      BinaryTree(None),
      BinaryTree([None]),
      BinaryTree([None, None, None]), sep='')
"""
Single Ton Binary Tree:
    - A Tree with only 1 Node
    - A Binary Tree whose leaf Nodes have NULL value 

>>> Height = 0
>>> Total Nodes = 1

Examples:
"""
print(BinaryTree([1]),
      BinaryTree([7, None, None]), sep='')
"""
Perfect Bin Tree:
    - All levels are completely filled. 
    - All internal nodes have strictly 2 children 
    - All leaf nodes are in same level.
    - All NULL / Empty Binary Trees are Perfect Binary Trees
      but all Perfect Binary Trees are not Empty Binary Trees 
    - All SingleTon Binary Trees are Perfect Binary Trees 
      but all Perfect Binary Trees are not SingleTon Binary Trees

>>> if Height = H
>>> Total Nodes = 2^(H + 1) - 1

>>> if Total Nodes = N
>>> Height = log(N + 1) - 1

>>> Leaf Nodes: 2^H
Examples:
"""
print(BinaryTree([]),  # A NULL Perfect Binary Tree
      BinaryTree([1]),  # A singleton Perfect Binary Tree
      BinaryTree([*range(1, 2 ** 4)]),  # A Perfect Binary Tree nut neither NULL nor SingleTon
      sep='')
"""
Full Binary Tree:
    - Every Node must have 0 or 2 children.
    - All Perfect Binary Trees are Full Binary Trees.
      but all full Binary Trees are not Perfect Binary Trees.
>>> if Height = H
>>> Total_Nodes = [2*H + 1, 2^(H + 1) - 1] 

>>> if Total Nodes = N
>>> Height = [log(N + 1) - 1, (N - 1) / 2]    

Examples:
"""
print(BinaryTree([*range(2 ** 3 - 1)]),  # All Perfect Binary Trees are Full Binary Trees
      BinaryTree([1, 2, 3, None, None, 4, 5]),  # All Full Binary Trees are not Perfect Binary Trees
      BinaryTree([*range(9)]),  # This is a Full & Complete Binary Tree but not always
      BinaryTree([*range(7), None, None, 8, 9]),  # This is a Full Binary Tree but not Complete Binary Tree
      sep='')

"""
Complete Binary Tree:
    - Every level is filled except the last level.
    - Every level is filled as left as possible.
    - All Perfect Binary Trees are Complete Binary Trees
      but all Complete Binary Trees are not Perfect Binary Trees.

>>> if Height = H
>>> Total Nodes = [2^H, 2^(H + 1) - 1]

>>> if Total Nodes = H
>>> Height = [log(N + 1) - 1, log(N)]

Examples:
"""
print(BinaryTree([*range(7)]),  # All Perfect Binary Trees are Complete Binary Trees
      BinaryTree([*range(5)]),  # All Complete Binary Trees are not Perfect Binary Trees.
      BinaryTree([*range(9)]),  # This is a Complete & Full Binary Tree but not always
      BinaryTree([*range(4)]),  # This is a Complete Binary Tree but not Full Binary Tree
      sep='')
"""
Degenerate / Pathological Tree:
    - Every Parent has only 1 child either left or right
    - Every Empty and SingleTon Tree is a Degenerate Tree
      but every Degenerate Tree is not an Empty or SingleTon Tree 
    - Every Skew Tree is a Degenerate Tree
      but every Degenerate Tree is not a Skew Tree

>>> if Height = H
>>> Total Nodes = H

>>> if Total Nodes = N
>>> Height = N

Examples:
"""
print(BinaryTree([]),  # All Empty Trees are Degenerate Trees
      BinaryTree([1]),  # All SingleTon Trees are Degenerate Trees
      BinaryTree([1, 2, None, 3, None, 4]),  # All Left - Skew Trees are Degenerate Trees
      BinaryTree([1, None, 2, None, 3, None, 4]),  # All Right - Skew Trees are Degenerate
      BinaryTree([1, 2, None, None, 3, 4]),  # All Degenerate Trees are not Skew Trees
      BinaryTree([1, None, 2, 3, None, None, 5]),  # A Degenerate Tree which is not a skew Tree
      sep='')
"""
Skew Tree:
    - Right Skewed Tree: A Tree which is dominated Solely by left child OR Every parent has only a left subtree  
    - Left Skewed: A Tree which is dominated Solely by right child OR Every Parent has only a right subtree

>>> if Height = H
>>> Total Nodes = H

>>> if Total Nodes = N
>>> Height = N

Examples:
"""
print(BinaryTree())
"""
Balanced Binary Tree:
    - A Tree which has an absolute difference <= 1 of number of left child child and number of right child in all 
      nodes  
    - All Perfect Binary Trees are Balanced Binary Trees
      but all Balanced Binary Trees are not Perfect Binary Trees 

>>> Height = H 
>>> Total Nodes = [(Total Nodes in Left SubTree + Total Nodes in Right SubTree + 1) , 2^H - 1]

Examples:
"""
print(BinaryTree([1, 2, 3, 4, 7, None, 5]))
print(BinaryTree([1, 2, 3, 4, None, None, 5]))

from datastax.Trees import BinaryTree

print(BinaryTree())

print(BinaryTree(),
      BinaryTree([]),
      BinaryTree(None),
      BinaryTree([None]),
      BinaryTree([None, None, None]))
print(BinaryTree(range(1, 32)))