from operator import itemgetter


class Node:
    def __init__(self, capacity, node_id, children=None, parent=None):
        if children is None:
            children = []
        self.capacity = capacity
        self.children = children
        self.parent = parent
        self.id = node_id

    def available_capacity(self):
        if self.children:
            return self.capacity - len(self.children)
        else:
            return self.capacity

    def __str__(self):
        return self.id


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.count = 1

    def add_node(self, node):
        if not self.root:
            self.root = node
            self.count = self.count + 1
        else:
            max_free_capacity_node = max(self.all_nodes(), key=itemgetter(1))[0]
            if max_free_capacity_node.capacity >= 1:
                node.parent = max_free_capacity_node
                max_free_capacity_node.children.append(node)
                self.count = self.count + 1
                max_free_capacity_node.capacity = max_free_capacity_node.capacity - 1
            else:
                return False
        return True

    def remove_node(self, node_id):
        node_to_remove = self.find_node_by_id(node_id)
        if not node_to_remove.parent:
            nodes_to_destruct = node_to_remove
            grand_parent = None
        else:
            nodes_to_destruct = node_to_remove.parent
            grand_parent = node_to_remove.parent.parent

        if grand_parent:
            grand_parent.children.remove(node_to_remove.parent)

        nodes_list = self.tree_to_list(nodes_to_destruct, [])
        nodes_list.remove(node_to_remove)
        sorted_nodes_list = sorted(nodes_list, key=lambda x: x.capacity, reverse=True)
        for x in sorted_nodes_list:
            self.add_node(x)
        return self

    """
    Helper utilities
    """

    def get_node_id(self):
        return f"N{self.count+1}"

    def all_nodes(self, level=0):
        nodes_list = list()
        nodes_list.append((self.root, self.root.available_capacity(), level))
        return Tree.get_child_nodes(self.root, nodes_list, level)

    @staticmethod
    def get_child_nodes(node, nodes_list, level):
        # nodes_list.append((node, node.available_capacity(), level))
        if node.children:
            level = level - 1
            for child in node.children:
                nodes_list.append((child, child.available_capacity(), level))
            for child in node.children:
                Tree.get_child_nodes(child, nodes_list, level)
        return nodes_list

    def find_node_by_id(self, node_id):
        return list(filter(lambda x: node_id == x[0].id, self.all_nodes()))[0][0]

    @staticmethod
    def tree_to_list(node, nodes_list):
        # Given a node, break down tree to a list of nodes from that point
        node.parent = None
        nodes_list.append(node)
        for x in range(len(node.children)):
            child = node.children[x]
            nodes_list = Tree.tree_to_list(child, nodes_list)
        node.children = []
        if node.children:
            node.capacity = node.capacity + len(node.children)
        return nodes_list

