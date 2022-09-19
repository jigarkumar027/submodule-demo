'''stack data structure '''
''' time complexity :---> o(1) , push and pop operation '''

def createStack():
    stack = []
    return stack

def push(stack , data):
    stack.append(data)
    return stack

def pop(stack):
    if check_empty(stack) == True:
        return 'stack is empty'
    return stack.pop()

def check_empty(stack):
    return len(stack) == 0

def numberOfTop(stack):
    return stack[-1]

stack = createStack()
stack = push(stack,10)
stack = push(stack,20)
stack = push(stack,30)
print('popped items:',stack.pop())
print('check stack:',check_empty(stack))
print('stack:',stack)