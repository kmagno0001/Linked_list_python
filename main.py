from linked_list import Linked_list
from node import Node


lst = Linked_list(10)
lst.append(55)
lst.append(5)
lst.append(9, 2)
lst.append(8, 3)
lst.append(7)



print(lst)

print(lst.get_nth_last_node(3))