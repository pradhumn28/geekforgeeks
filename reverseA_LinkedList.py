class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def ReverseA_Linklist(linklist):
    prev = linklist.head
    next = prev.next
    prev.next = None
    while next:
        temp = next.next
        next.next = prev
        linklist.head = next
        prev = next
        next = temp
    return linklist

def printList(linklist):
    temp = linklist.head
    while temp:
        print(temp.data)
        temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(10):
        if i == 0:
            temp1 = Node(i)
            llist.head = temp1
        else:
            temp = Node(i)
            temp1.next = temp
            temp1 = temp1.next 
    printList(llist)
    ReverseA_Linklist(llist)
    printList(llist)
