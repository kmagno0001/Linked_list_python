class Node:
    def __init__(self, value:int, next_node = None) -> None:
        self.value = value
        self.next_node: Node = next_node

    def get_value(self) -> int:  
        return self.value
    
    def get_next_node(self): 
        return self.next_node

    def set_next_node(self, node) -> None:
        self.next_node: Node = node
