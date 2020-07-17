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
            print(s, end=" ")

            # si el nodo no esta en CERRADO y su padre no es el mismo
            closedd.append(s)
            print("get succesorsss")
            successors = Operations.getSuccesors(
                self, rules, s, node_num, closedd)
            if len(successors) > 0:
                node_num = successors[len(successors)-1][0][0]
            else:
                print("no hay sucesores")
                
            # Si algun sucesor es el estado final
            for node in successors:
                if Operations.compare2Matrix(node[1], end_state):
                    flag_end_state = True
                    closedd.append(node)
                # si no son el estado final
                else:
                    openn.append(node)

        total_nodes = len(closedd)
        res['total_nodes'] = total_nodes
        res['route'] = Operations.getWaytoEndState(closedd)
        print("solucion encontrada  "+str(total_nodes))
        return res

    def bpp(self, init_state, end_state, bpp_limit):
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
        flag_no_answer = False
        openn.append(current_node)
        counter = 0
        # Mientras ABIERTO no esté vacia y el estado final no se haya alcanzadop
        while openn and flag_end_state == False and flag_no_answer==False:
            counter += 1
            s = openn.pop(0)
            print(s, end=" ")

            # si el nodo no esta en CERRADO (Se valida en los sucesores) y su padre no es el mismo 
            if s[0][2]<=bpp_limit:
                closedd.append(s)
                print("get succesorsss")
                successors = Operations.getSuccesors(
                    self, rules, s, node_num, closedd)
                if len(successors) > 0:
                    node_num = successors[len(successors)-1][0][0]
                else:
                    print("no hay sucesores")
                    # node_num = successors[0][0][0]
                    
                    
                # Si algun sucesor es el estado final
                for node in successors:
                    if Operations.compare2Matrix(node[1], end_state):
                        flag_end_state = True
                        closedd.append(node)
                    # si no son el estado final
                    else:
                        openn.insert(0,node)
            else:
                print("Se llegó al limite sin encontrar respuesta")
                flag_no_answer = True

            
        if flag_no_answer==False:
            total_nodes = len(closedd)
            res['total_nodes'] = total_nodes
            res['route'] = Operations.getWaytoEndState(closedd)
        else:
            res['total_nodes'] = 'Indeterminado'
            res['route'] = 'Sin ruta encontrada por el limite de profundidad'
            

        return res

    def hill_climbing(self, init_state, end_state):
        return 3

    def branch(self, init_state, end_state):
        return 4

    def asterisk(self, init_state, end_state):
        return 5

    def genetic(self, init_state, end_state):
        return 6
