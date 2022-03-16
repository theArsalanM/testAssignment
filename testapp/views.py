import requests
from django.http import JsonResponse
from rest_framework.views import APIView

from testapp.tree import Tree, Node

tree = Tree()


class AddNode(APIView):
    def post(self, request, capacity):
        tree.add_node(Node(capacity=capacity, node_id=tree.get_node_id()))
        return JsonResponse({'success': True, 'message': 'Node added'})


class ViewTree(APIView):
    # TODO:
    # WIP
    def get(self, request):
        nodes = tree.tree_print()
        json_response = list()
        temp_list = list()
        if nodes:
            for node in nodes:
                if node == '-':
                    json_response.append(temp_list)
                    temp_list = list()
                else:
                    temp_list.append(node)

        return JsonResponse({'data': json_response})
