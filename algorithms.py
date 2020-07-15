from rules import Rules
from operations import Operations
import numpy as np


class Algorithms:

    def __init__(self):
        print("--")

    def testMethod(self, data):
        print("-----------")
        rr = Rules.getRule(self)
        return rr

    def bpa(self, init_state, end_state):
        node_num = 1
        node_father = 0
        level = 0
        operator = None
        current_node = [[node_num, node_father, level, operator], init_state]
        total_nodes = 0
        nodes_route = []
        rules = Rules.getRule(self)
        res = {}

        closedd = []  # Lista que mantiene historia de los nodos visitados
        openn = []  # Inicializa la cola
        successors = []
        flag_end_state = False
        openn.append(current_node)
        counter = 0
        # Mientras ABIERTO no esté vacia y el estado final no se haya alcanzadop
        while openn and flag_end_state == False:
            counter += 1
            s = openn.pop(0)
            # print (s, end = " ")

            # si el nodo no esta en CERRADO y su padre no es el mismo
            if len(closedd)>0:
                # route = Operations.getRoute(closedd,s)
                # flag_repeated = False
                # for rr in route:
                #     if Operations.compare2Matrix(rr[1],s[1]):
                #         flag_repeated = True
                
                # if flag_repeated==False:
                #     print("get succesorssss")
                #     successors = Operations.getSuccesors(self, rules, s,node_num,closedd)
                #     node_num = successors[len(successors)-1][0][0]
                # equal_array = False
                for cl in closedd:
                    equal_arr = Operations.compare2Matrix(s[1], cl[1])
                    if equal_arr == False and s[0][1] != cl[0][1]:
                        closedd.append(s)
                        print("get succesors")
                        successors = Operations.getSuccesors(self, rules, s,node_num,closedd)
                        node_num = successors[len(successors)-1][0][0]
            else:
                closedd.append(s)
                print("get succesors")
                successors = Operations.getSuccesors(self, rules, s,node_num,closedd)
                node_num = successors[len(successors)-1][0][0]
                # print(successors)

            # Si algun sucesor es el estado final
            for node in successors:
                if Operations.compare2Matrix(node[1],end_state):
                    flag_end_state = True
                    closedd.append(node)
                # si no son el estado final
                else:
                    for cl in closedd:
                        if Operations.compare2Matrix(cl[1], node[1]) == False and cl[0][1] != node[0][1]:
                            openn.append(node)
                            break
        
        total_nodes = len(closedd)
        res['total_nodes'] = total_nodes
        res['route'] = Operations.getWaytoEndState(closedd)

        return res

    def bpp(self, init_state, end_state, bpp_limit):
        return 2

    def hill_climbing(self, init_state, end_state):
        return 3

    def branch(self, init_state, end_state):
        return 4

    def asterisk(self, init_state, end_state):
        return 5

    def genetic(self, init_state, end_state):
        return 6
