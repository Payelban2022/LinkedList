class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data) + '-->'
            itr = itr.next
        print(liststr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

if __name__=='__main__':
    ll = linked_list()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(60)
    ll.print()



