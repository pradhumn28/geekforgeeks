class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

def printList(llist): 
    temp = llist.head 
    while (temp): 
        print(temp.data) 
        temp = temp.next


def insertAtEnd(llist, el):
    temp = llist.head
    tempNode = Node(el)
    while(temp.next):
        temp = temp.next
    temp.next = tempNode
    return llist


def insertionAtStart(llist, el):
    temp = llist.head
    tempNode = Node(el)
    llist.head = tempNode
    llist.head.next = temp
    return llist


def insertionAtNthPosition(llist, el, pos):
    temp = llist.head
    tempNode = Node(el)
    for i in range(pos-1):
        if not temp:
            return llist
        temp = temp.next
    tempNode1 = temp.next
    tempNode.next = tempNode1
    temp.next = tempNode
    return llist

if __name__ == '__main__':
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist = insertAtEnd(llist,4)
    llist = insertionAtStart(llist,5)
    llist = insertionAtNthPosition(llist,6,2)
    printList(llist)