# Stack (LIFO)
stack = []
stack.append(4) # [4]
stack.append(5) # [4, 5]
stack.append(6) # [4, 5, 6]
stack.append(7) # [4, 5, 6, 7]
print(stack)

stack.pop() # [4, 5, 6]
print(stack)

stack.append(8) # [4, 5, 6, 8]
print(stack)


# Queue (FIFO)
from collections import deque

queue = deque()
queue.append(4) # [4]
queue.append(5) # [4, 5]
queue.append(6) # [4, 5, 6]
queue.append(7) # [4, 5, 6, 7]
print(queue)

queue.popleft() # [5, 6, 7]
print(queue)

queue.append(8) # [5, 6, 7, 8]
print(queue)


# Recursive
def recursive(n):
    if n == 10:
        return 
    print(f"{n} th function")
    recursive(n+1)

recursive(1)

# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))