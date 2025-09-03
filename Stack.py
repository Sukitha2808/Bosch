class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.data

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.data

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    if self.isEmpty():
        print("Stack is empty.")
        return

    currentNode = self.head
    elements = []
    while currentNode:
      elements.append(str(currentNode.data))
      currentNode = currentNode.next
    print(" -> ".join(elements))

'''''    currentNode = self.head
    while currentNode:
      print(currentNode.data, end=" -> ")
      currentNode = currentNode.next
    print()'''''
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')
myStack.push('E')

print("Stack: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("Stack after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())

