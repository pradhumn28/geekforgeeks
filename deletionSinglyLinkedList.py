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


def deletionOfElement(llist,el):
    temp = llist.head
    while temp and temp.data is not el:
        prev = temp
        temp = temp.next
    if temp:
        deletNode = temp
        prev.next = deletNode.next
        deletNode = None
    return llist


def deletionAtPos(llist, pos):
    temp = llist.head
    for i in range(pos-1):
        if not temp:
            break
        prev = temp
        temp = temp.next
    if temp:
        prev.next = temp.next
        temp = None
    return llist


if __name__ == "__main__":
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    third.next=Node(5)
    deletionOfElement(llist,3)
    deletionAtPos(llist,2)
    printList(llist)
