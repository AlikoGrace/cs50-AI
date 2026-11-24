
# ******************* LAST IN LASRT OUT /For DFS*************
stack=[]
stack.append("plate1")
stack.append("plate2")
stack.append("plate3")
print(f"the fist to come off is : {stack.pop()}")
print(stack)


# ******************* FIRST IN FIRST OUT/ FOR BFS*************
from collections import deque

queue=deque()
queue.append("Ama")
queue.append("kofi")
queue.append("Esi")
print(f"the fist to come off is : {queue.popleft()}")
print(list(queue))
