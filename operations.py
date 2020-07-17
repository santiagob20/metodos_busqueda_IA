import copy
import numpy as np

class Operations:
    def __init__(self):
        None
    

    
    def compareCloseddAndSuccesor(self,listCerrado,node):
        flag_repeated = False
        route = Operations.getRoute(listCerrado,node)
        arr1 = np.array(node[1])
        
        for i in route:
            arr2 = np.array(i[1])
            compare = arr1 == arr2
            if compare.all():
                flag_repeated = True
                break
        return flag_repeated
    
    def compare2Matrix(mat1,mat2):
        arr1 = np.array(mat1)
        arr2 = np.array(mat2)
        compare = arr1== arr2
        equal_arr = compare.all()
        return equal_arr
    
    def getSuccesors(self,rules, node,current_number_node,closedd):
        opp = Operations()
        succesors = []
        node_info = copy.copy(node[0])
        father = node_info[0]
        current_node = []
        numm = current_number_node
        
    
        for i in range(len(node[1])):
            for j in range(len(node[1][i])):
                if node[1][i][j]=='0':
                    for rule in rules:
                        current_node = []
                        current_node = copy.deepcopy(node)
                        
                        if rule['id']==0:
                            # se intenta mover a la derecha
                            if j<len(current_node[1][i])-1:
                                tmp = current_node[1][i][j+1]
                                current_node[1][i][j+1] = current_node[1][i][j]
                                current_node[1][i][j] = tmp
                                ##se crea un sucesor
                                numm = numm+1
                                new_node_info = [numm,father,node_info[2]+1,rule['id']]
                                node_info[0]= node_info[0]+1
                                if opp.compareCloseddAndSuccesor(closedd,[new_node_info,current_node[1]])==False:
                                    succesors.append([new_node_info,current_node[1]])
                        if rule['id']==1:
                            # se intenta mover abajo
                            if i<len(current_node[1])-1:
                                tmp = current_node[1][i+1][j]
                                current_node[1][i+1][j] = current_node[1][i][j]
                                current_node[1][i][j] = tmp
                                ##se crea un sucesor
                                numm = numm+1
                                new_node_info = [numm,father,node_info[2]+1,rule['id']]
                                node_info[0]= node_info[0]+1
                                if opp.compareCloseddAndSuccesor(closedd,[new_node_info,current_node[1]])==False:
                                    succesors.append([new_node_info,current_node[1]])                         
                        if rule['id']==2:
                            # se intenta mover a la izquierda
                            if j>0:
                                tmp = current_node[1][i][j-1]
                                current_node[1][i][j-1] = current_node[1][i][j]
                                current_node[1][i][j] = tmp
                                ##se crea un sucesor
                                numm = numm+1
                                new_node_info = [numm,father,node_info[2]+1,rule['id']]
                                node_info[0]= node_info[0]+1
                                if opp.compareCloseddAndSuccesor(closedd,[new_node_info,current_node[1]])==False:
                                    succesors.append([new_node_info,current_node[1]])
                        if rule['id']==3:
                            # se intenta mover arriba
                            if i>0:
                                tmp = current_node[1][i-1][j]
                                current_node[1][i-1][j] = current_node[1][i][j]
                                current_node[1][i][j] = tmp
                                ##se crea un sucesor
                                numm = numm+1
                                new_node_info = [numm,father,node_info[2]+1,rule['id']]
                                node_info[0]= node_info[0]+1
                                if opp.compareCloseddAndSuccesor(closedd,[new_node_info,current_node[1]])==False:
                                    succesors.append([new_node_info,current_node[1]])
        # print('--------')                                        
        # print(succesors)                                        
        return succesors
    
    def getWaytoEndState(listCerrado):
        end_state = listCerrado[len(listCerrado)-1]
        father = end_state[0][1]
        route = []
        tmproute = []
        counter = len(listCerrado)-1
        while counter >=0:
            if father == listCerrado[counter][0][0]:
                tmproute.append(listCerrado[counter])
                father = listCerrado[counter][0][1]
            counter = counter-1
        tmproute.append(end_state)
        route = sorted(tmproute,reverse=False)
        return route
    
    def getRoute(listCerrado,current_node):
        end_state = copy.deepcopy(current_node)
        father = end_state[0][1]
        route = []
        counter = len(listCerrado)-1
        while counter >=0:
            if father == listCerrado[counter][0][0]:
                route.append(listCerrado[counter])
                father = listCerrado[counter][0][1]
            counter = counter-1
        # route.append(end_state)
        return sorted(route,reverse=False)
    
    