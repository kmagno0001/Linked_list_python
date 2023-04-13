from node import Node

class Linked_list:
    def __init__(self, value = None) -> None:
        self.head_node = Node(value)
        self.len = 1

    def append(self, new_value: int, index: int = None) -> None:
         
        iterator_node = self.head_node

        if index == None:
            while iterator_node.get_next_node() != None:
                iterator_node = iterator_node.get_next_node()
                
            iterator_node.set_next_node(Node(new_value)) 
        elif index < self.len:     
            counter: int = 0
            prev_node: Node = self.head_node

            while iterator_node.get_next_node() != None:
                if index == counter:
                    break
                prev_node = iterator_node    
                iterator_node = iterator_node.get_next_node()
                counter += 1

            if index == 0:
                self.head_node = Node(new_value, iterator_node)
            else:
                prev_node.set_next_node(Node(new_value, iterator_node)) 
        else:
            return    
           
        self.len += 1  

    def __repr__(self) -> str:
        tmp = ''
        iterator_node = self.head_node
        while iterator_node.get_next_node() != None:
            tmp +=  f"{iterator_node.get_value()} "
            iterator_node = iterator_node.get_next_node()
        else:
            tmp += f"{iterator_node.get_value()} "

        return tmp
    
    def get_nth_last_node(self, nth: int) -> int :
        last: Node = None
        iter_node: Node = self.head_node
        count: int = 1
        while iter_node != None:
            iter_node = iter_node.get_next_node()
            count += 1

            if count >= nth + 1 :
                if last is None:
                    last = self.head_node
                else:
                    last = last.get_next_node()
        return last.get_value()                




