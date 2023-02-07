class Node:
    def __int__(self,value=None):
        self.value = value
        self.next = next

class Linkedlist:
    def __int__(self):
        self.head = None

    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode
        curnode = curnode.next

class Stack:
    def __int__(self):
        self.linkedlist = Linkedlist()

    def __str__(self):
        value = [str(x) for x in self.linkedlist]
        return "\n".join(values)

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.linkedlist.head
        self.linkedlist.head = node

    def popmeth(self):
        if self.isEmpty():
            return 'there not any element in the stack'
        else:
            nodevalue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodevalue


customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
customstack.push(5)
customstack.popmeth()
print(customstack)