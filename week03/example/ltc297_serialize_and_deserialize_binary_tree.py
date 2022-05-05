# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        seq_list = []

        def dfs(root):
            if root is None:
                seq_list.append("None")
                return
            seq_list.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(seq_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        seq_list = data.split(",")
        curr = 0

        def restore():
            nonlocal curr
            if seq_list[curr] == "None":
                curr += 1
                return
            root = TreeNode(int(seq_list[curr]))
            curr += 1
            root.left = restore()
            root.right = restore()
            return root

        return restore()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
