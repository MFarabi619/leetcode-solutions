# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Initialize a queue with the root and a list to store the result
        queue = deque([root])
        result = []
        
        while queue:
            # Get the current level size
            level_size = len(queue)
            current_level = []
            
            # Process all nodes in the current level
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result