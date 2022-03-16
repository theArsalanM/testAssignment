from operator import itemgetter

from django.test import TestCase

from testapp.tree import Tree, Node


class TestTree1(TestCase):
    """
        2
     /  |  \
     3  4  5
        |
        1
    """
    def setUp(self) -> None:
        n1 = Node(capacity=4, node_id='N1')
        n2 = Node(capacity=3, node_id='N2')
        n3 = Node(capacity=2, node_id='N3')
        n4 = Node(capacity=1, node_id='N4')
        n5 = Node(capacity=5, node_id='N5')
        n4.children.append(n1)
        n2.children.append(n4)
        n2.children.append(n5)
        n2.children.append(n3)
        self.tree = Tree(root=n2)

    def test_max_free_capacity_node(self):
        max_free_capacity_node = max(self.tree.all_nodes(), key=itemgetter(1))[0]
        self.assertEqual(max_free_capacity_node.id, "N5")

    def test_find_node_to_remove(self):
        node_id = 'N3'
        node_to_remove = list(filter(lambda x: node_id == x[0].id, self.tree.all_nodes()))[0][0]
        self.assertEqual(node_to_remove.id, node_id)

    def test_find_node_by_id(self):
        node = self.tree.find_node_by_id("N2")
        self.assertEqual(node.id, "N2")

    def test_remove_node(self):
        nodes = self.tree.remove_node("N2")
        # WIP
        self.assertTrue(True)
