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



if __name__ == '__main__':
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist = insertAtEnd(llist,4)
    printList(llist)