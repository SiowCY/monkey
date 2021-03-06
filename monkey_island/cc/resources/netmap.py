import flask_restful

from cc.services.edge import EdgeService
from cc.services.node import NodeService
from cc.database import mongo

__author__ = 'Barak'


class NetMap(flask_restful.Resource):
    def get(self, **kw):
        monkeys = [NodeService.monkey_to_net_node(x) for x in mongo.db.monkey.find({})]
        nodes = [NodeService.node_to_net_node(x) for x in mongo.db.node.find({})]
        edges = [EdgeService.edge_to_net_edge(x) for x in mongo.db.edge.find({})]

        if NodeService.get_monkey_island_monkey() is None:
            monkey_island = [NodeService.get_monkey_island_pseudo_net_node()]
            edges += EdgeService.get_monkey_island_pseudo_edges()
        else:
            monkey_island = []
            edges += EdgeService.get_infected_monkey_island_pseudo_edges()

        return \
            {
                "nodes": monkeys + nodes + monkey_island,
                "edges": edges
            }


