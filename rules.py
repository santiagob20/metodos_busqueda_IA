import copy
import random


class Rules:
    def __init__(self):
        print("init")

    def getRule(self):
        rules = [{
            "id": 2, "description": "Movimiento izquierda"}, {"id": 3, "description": "Movimiento arriba"}, {"id": 1, "description": "Movimiento abajo"},{"id": 0, "description": "Movimiento derecha"}]
        random.shuffle(rules)
        return rules
