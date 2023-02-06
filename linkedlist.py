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
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
       count = 0
       itr = self.head
       while itr:
           count += 1
           itr = itr.next
       return count


if __name__=='__main__':
    ll = linked_list()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(60)
    ll.insert_values(["bananas","mangoes","grapes","oranges"])
    print("length:",ll.get_length())
    ll.print()




