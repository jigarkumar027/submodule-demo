# '''Linked List '''

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def sortll(head):
    current = head
    index = Node(None)

    if head is None:
        return
    else:
        while current is not None:
            index = current.next

            while index is not None:
                if current.item > index.item:
                    current.item, index.item = index.item, current.item
                index = index.next
            current = current.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(33)
    third = Node(2)

    # connect nodes
    linked_list.head.next = second
    second.next = third

    #insert at the beginning 
    # first = Node(0)
    # first.next = linked_list.head
    # linked_list.head = first
    
    #insert at the end
    # newlast = Node(4)
    # third.next = newlast

    #insert at the 2nd position
    # index = 3
    # indexcount = 0
    # for i in range(index-1):
    #     print(linked_list.head.item,end='***')
    #     linked_list.head = linked_list.head.next
    # newnumber = Node(11)
    # newnumber.next = linked_list.head.next
    # linked_list.head.next = newnumber 
     
    #to delete the perticular listnumber
    #delete from the beginnig
    # linked_list.head = linked_list.head.next

    # printing the linked list
    sortll(linked_list.head)

    while linked_list.head != None:
        print(linked_list.head.item,end='-->')
        linked_list.head = linked_list.head.next
        