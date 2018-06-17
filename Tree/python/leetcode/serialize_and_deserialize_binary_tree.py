"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms
should be stateless.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes = list()
        stack = list()
        stack.append(root)
        nodes.append(root)
        while stack:
            root = stack.pop(0)
            left, right = root.left, root.right
            nodes.append(left)
            nodes.append(right)
            if left:
                stack.append(left)
            if right:
                stack.append(right)

        while nodes and nodes[-1] is None:
            nodes.pop()

        data = list()
        for node in nodes:
            if node:
                data.append(str(node.val))
            else:
                data.append('null')

        return str(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = [None if val == 'null' else TreeNode(int(val)) for val in data.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


codec = Codec()
print(codec.serialize(codec.deserialize("[1,2,3,null,null,4,5]")))


'''
leetcode discuss solution:

The idea is simple: print the tree in pre-order traversal and use "X" to denote null node and split node with ",". 
We can use a StringBuilder for building the string on the fly. For deserializing, we use a Queue to store the 
pre-order traversal and since we have "X" as null node, we know exactly how to where to end building subtress.

public class Codec {
    private static final String spliter = ",";
    private static final String NN = "X";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append(NN).append(spliter);
        } else {
            sb.append(node.val).append(spliter);
            buildString(node.left, sb);
            buildString(node.right,sb);
        }
    }
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(spliter)));
        return buildTree(nodes);
    }
    
    private TreeNode buildTree(Deque<String> nodes) {
        String val = nodes.remove();
        if (val.equals(NN)) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(nodes);
            node.right = buildTree(nodes);
            return node;
        }
    }
}
'''
